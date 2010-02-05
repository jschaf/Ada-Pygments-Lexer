"""
    Portions of this file are covered under the following license:
    
    :copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.

    The rest of the work is placed in the public domain.
"""

import re

from pygments.lexer import Lexer, DelegatingLexer, RegexLexer, bygroups, \
     include, using, this

from pygments.lexer import RegexLexer
from pygments.token import *

class AdaLexer(RegexLexer):
    """
    For Ada source code.
    """

    name = 'Ada'
    aliases = ['ada', 'ada95' 'ada2005']
    filenames = ['*.adb', '*.ads', '.ada']
    mimetypes = ['text/x-ada']

    flags = re.MULTILINE | re.I

    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'

    tokens = {
        'root': [
            (r'[^\S\n]+', Text),
            (r'--.*?\n', Comment.Single),
            (r'[^\S\n]+', Text),
            (r'(true|false|null)\b', Keyword.Constant),
            (r'\b(abort|abs|abstract|accept|access|aliased|all|array|at|begin|body|case|constant|declare|delay|delta|digits|do|else|elsif|end|entry|exception|exit|interface|for|goto|if|is|limited|loop|new|null|of|others|out|overriding|pragma|protected|raise|range|record|renames|requeue|return|reverse|select|separate|synchronized|task|tagged|terminate|then|until|when|while|xor)\b',
             Keyword.Reserved),
            (r'Byte|Character|Float|Integer|Long_Float|Long_Integer|Long_Long_Float|Long_Long_Integer|Natural|Positive|Short_Float|Short_Integer|Short_Short_Float|Short_Short_Integer|String|Wide_String|Duration', Keyword.Type),
            (r'\b(and|in|mod|not|or|rem)\b', Operator.Word),
            (r'generic|private', Keyword.Declaration),
            (r'(function|package|procedure|subtype|type)(\s+)', bygroups(Keyword.Declaration, Text), 'identifier'),
            # (r'type|package', Keyword.Declaration),
            (r'(with|use)(\s+)', bygroups(Keyword.Namespace, Text), 'import'),
            (r'([a-z0-9_]+)(\s*)(:)(\s*)(constant)', bygroups(Name.Constant, Text, Punctuation, Text, Keyword.Reserved)),
            (r'([a-z0-9_]+)(\s*)(:)', bygroups(Name.Variable, Text, Punctuation)),
            (r'"[^"]*"', String),
            (r"'[^']'", String.Character),
            (r'16#[0-9a-f][0-9a-f_]*#', Number.Hex),
            (r'[0-9]+#[0-9a-f][0-9a-f_]*#', Number),
            (r'([a-z0-9_]+)(\s*|[(,])', bygroups(Name, using(this))),
            (r"(<>|=>|:=|[\(\)\|:;,.'])", Punctuation),
            (r'[*<>+=/&-]', Operator),
            (r'[0-9][0-9_]*', Number.Integer),
            (r'\n', Text)
            
        ],
        'identifier': [
            (r'("[^"]+"|[a-z0-9_]+)', Name.Function, '#pop')
        ],
        'import': [
            (r'[a-z0-9_.]+', Name.Namespace, '#pop')
        ]
        # 'class': [
        #     (r'([a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]|[a-zA-Z])', Name.Class, '#pop')
        #     ]
        }

