# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '大草的读书笔记'
copyright = '2023, da1234cao'
author = 'da1234cao'
release = 'latest'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx_comments'
]

comments_config = {
   "utterances": {
      "repo": "da1234cao/dacao-reading-notes",
      "issue-term": "pathname",
      "label": "comment",
      "theme": "github-light"
   }
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 修改在github上编辑的链接;而非打开编译生成的文件
# ref: https://docs.readthedocs.io/en/stable/guides/edit-source-links-sphinx.html
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "da1234cao",  # Username
    "github_repo": "dacao-reading-notes",  # Repo name
    "github_version": "laboratory",  # Version
    "conf_py_path": "/source/",  # Path in the checkout to the docs root
}
