" These will make vim open with default settings, then this file will be used to customize on top of that.
" See :help defaults.vim for more information
unlet! skip_defaults_vim
source $VIMRUNTIME/defaults.vim


" Keeping extra files in one directory [ // makes file names include paths to avoid collisions]
" PLEASE MAKE SURE THE DIRECTORIES EXIST FOR THIS TO WORK
set backupdir=$HOME/.vim/backup//
set directory=$HOME/.vim/swap//
set undodir=$HOME/.vim/undo//
" Force to keep these files
set backup
set swapfile
set undofile

" For line numbers
set nu
set relativenumber

" Tabs and spaces
set tabstop=4 softtabstop=4
set shiftwidth=4
set noexpandtab

" Set colorscheme
colorscheme delek

" Do highlight search queries
set hlsearch
set incsearch
" change highlight colors
hi Search ctermbg=236
hi Search ctermfg=LightGray

" Opening multiple buffers in vim without saving each
set hidden

" Search queries ignorecase when all is small. Not when something is capital
set smartcase
set ignorecase

" Set scroll margin to 8 lines
set scrolloff=8

" highlight colors
autocmd VimEnter * ColorHighlight
