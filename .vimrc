call plug#begin()

Plug 'sainnhe/everforest'
Plug 'tpope/vim-commentary'
Plug 'preservim/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'dmerejkowsky/vim-ale'
Plug 'romgrk/doom-one.vim'

call plug#end()

set background=dark
colorscheme doom-one

syntax on
set nu
set ruler
set backspace=indent,eol,start
set showcmd
set incsearch
set hlsearch
set tabstop=4

set mouse=a
