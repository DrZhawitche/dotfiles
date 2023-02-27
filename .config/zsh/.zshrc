export PATH="$HOME/.emacs.d/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export ZSHDIR="$HOME/.config/zsh/"

PAGER=less

#Prompt

autoload -Uz vcs_info
precmd() { vcs_info }
zstyle ':vcs_info:git:*' formats '%b '
setopt PROMPT_SUBST

PROMPT='%F{green}%B%n@%F{magenta}%m%f %B%F{248}%1~%f%b %# '

autoload -Uz compinit
compinit

#Plugins and aliases
source $HOME/.config/shell/aliasrc
source $ZSHDIR/plugins/synthax.zsh 
source $ZSHDIR/plugins/autosuggestions.zsh 

# Startup
pfetch
