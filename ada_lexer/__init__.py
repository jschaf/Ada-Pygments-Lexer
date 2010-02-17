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
    filenames = ['*.adb', '*.ads', '*.ada']
    mimetypes = ['text/x-ada']

    flags = re.MULTILINE | re.I # Ignore case

    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'

    tokens = {
        'root': [
            (r'[^\S\n]+', Text),
            (r'--.*?\n', Comment.Single),
            (r'[^\S\n]+', Text),
            (r'function|procedure|entry', Keyword.Declaration, 'subprogram'),
            (r'(subtype|type)(\s+)([a-z0-9_]+)',
             bygroups(Keyword.Declaration, Text, Keyword.Type), 'type_def'),
            (r'task|protected', Keyword.Declaration),
            (r'(subtype)(\s+)', bygroups(Keyword.Declaration, Text)),
            (r'(end)(\s+)', bygroups(Keyword.Reserved, Text), 'end'),
            (r'(pragma)(\s+)([a-zA-Z0-9_]+)', bygroups(Keyword.Reserved, Text,
                                                       Comment.Preproc)),
            (r'(true|false|null)\b', Keyword.Constant),
            (r'(Byte|Character|Float|Integer|Long_Float|Long_Integer|'
             r'Long_Long_Float|Long_Long_Integer|Natural|Positive|Short_Float|'
             r'Short_Integer|Short_Short_Float|Short_Short_Integer|String|'
             r'Wide_String|Duration)\b', Keyword.Type),
            (r'(and(\s+then)?|in|mod|not|or(\s+else)|rem)\b', Operator.Word),
            (r'generic|private', Keyword.Declaration),
            (r'package', Keyword.Declaration, 'package'),
            (r'array\b', Keyword.Reserved, 'array_def'),
            (r'(with|use)(\s+)', bygroups(Keyword.Namespace, Text), 'import'),
            (r'([a-z0-9_]+)(\s*)(:)(\s*)(constant)',
             bygroups(Name.Constant, Text, Punctuation, Text,
                      Keyword.Reserved)),
            (r'<<[a-z0-9_]+>>', Name.Label),
            (r'([a-z0-9_]+)(\s*)(:)(\s*)(declare|begin|loop|for|while)',
             bygroups(Name.Label, Text, Punctuation, Text, Keyword.Reserved)),
            (r'\b(abort|abs|abstract|accept|access|aliased|all|array|at|begin|'
             r'body|case|constant|declare|delay|delta|digits|do|else|elsif|end|'
             r'entry|exception|exit|interface|for|goto|if|is|limited|loop|new|'
             r'null|of|or|others|out|overriding|pragma|protected|raise|range|'
             r'record|renames|requeue|return|reverse|select|separate|subtype|'
             r'synchronized|task|tagged|terminate|then|type|until|when|while|'
             r'xor)\b',
             Keyword.Reserved),
            (r'"[^"]*"', String),
            include('attribute'),
            include('numbers'),
            (r"'[^']'", String.Character),
            (r'([a-z0-9_]+)(\s*|[(,])', bygroups(Name, using(this))),
            (r"(<>|=>|:=|[\(\)\|:;,.'])", Punctuation),
            (r'[*<>+=/&-]', Operator),
            (r'\n+', Text)

        ],
        'numbers' : [
            (r'[0-9_]+#[0-9a-f]+#', Number.Hex),
            (r'[0-9_]+\.[0-9_]*', Number.Float),
            (r'[0-9_]+', Number.Integer)
        ],
        'attribute' : [
            (r"(')([a-zA-Z0-9_]+)", bygroups(Punctuation, Name.Attribute))
        ],
        'subprogram' : [
            (r'\(', Punctuation, ('#pop', 'formal_part')),
            (r';', Punctuation, '#pop'),
            (r'is\b', Keyword.Reserved, '#pop'),
            (r'"[^"]+"|[a-z0-9_]+', Name.Function),
            include('root')
        ],
        'end' : [
            ('(if|case|record|loop|select)', Keyword.Reserved),
            ('"[^"]+"|[a-zA-Z0-9_]+', Name.Function),
            ('[\n\s]+', Text),
            (';', Punctuation, '#pop'),
        ],
        'type_def': [
            (r';', Punctuation, '#pop'),
            (r'\(', Punctuation, 'formal_part'),
            (r'with|and|use', Keyword.Reserved),
            (r'array\b', Keyword.Reserved, ('#pop', 'array_def')),
            (r'record\b', Keyword.Reserved, ('formal_part')),
            include('root')
        ],
        'array_def' : [
            (r';', Punctuation, '#pop'),
            (r'([a-z0-9_]+)(\s+)(range)', bygroups(Keyword.Type, Text, Keyword.Reserved)),
            include('root')
        ],
        'import': [
            (r'[a-z0-9_.]+', Name.Namespace, '#pop')
        ],
        'formal_part' : [
            (r'\)', Punctuation, '#pop'),
            (r'([a-z0-9_]+)(\s*)(,|:[^=])', bygroups(Name.Variable, Text, Punctuation)),
            (r'(in|not|null|out|access)\b', Keyword.Reserved),
            include('root')
        ],
        'package': [
            ('body', Keyword.Declaration),
            ('is\s+new|renames', Keyword.Reserved),
            ('is', Keyword.Reserved, '#pop'),
            (';', Punctuation, '#pop'),
            ('\(', Punctuation, 'package_instantiation'),
            ('([a-zA-Z0-9_.]+)', Name.Class),
            include('root')
        ],
        'package_instantiation': [
            (r'("[^"]+"|[a-z0-9_]+)(\s+)(=>)', bygroups(Name.Variable, Text, Punctuation)),
            (r'[a-z0-9._\'"]', Text),
            (r'\)', Punctuation, '#pop'),
            include('root')
        ],
    }

