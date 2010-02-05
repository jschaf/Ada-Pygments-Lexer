"""Implementation of a Pygments Lexer for the Ada language."""

from setuptools import setup

__author__ = 'Joe'

setup(
    name='Ada Pygments Lexer',
    version='0.1',
    description=__doc__,
    author=__author__,
    packages=['ada'],
    entry_points='''
    [pygments.lexers]
    Ada = ada:AdaLexer
    '''
)
