"""Implementation of a Pygments Lexer for the Ada language."""

from setuptools import setup

__author__ = 'Joe'

setup(
    name='Ada Pygments Lexer',
    version='0.1.0',
    description=__doc__,
    author=__author__,
    packages=['ada_lexer'],
    entry_points='''[pygments.lexers]
adalexer = ada_lexer:AdaLexer
'''
)
