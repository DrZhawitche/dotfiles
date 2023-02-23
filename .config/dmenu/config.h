/* See LICENSE file for copyright and license details. */
/* Default settings; can be overriden by command line. */

static int topbar = 1;                      /* -b  option; if 0, dmenu appears at bottom     */
/* -fn option overrides fonts[0]; default X11 font or font set */
static const char *fonts[] = {
	"Cantarell:size=10"
};
static const char *prompt      = NULL;      /* -p  option; prompt to the left of input field */
static const char *colors[SchemeLast][2] = {
	                      /*     fg         bg       */
	[SchemeNorm] =          { "#d3c6aa", "#475258" },
	[SchemeSel] =           { "#1e2326", "#2d353b" },
	[SchemeSelHighlight] =  { "#e67e80", "#a7c080" },
	[SchemeNormHighlight] = { "#e67e80", "#343f44" },
	[SchemeOut] =           { "#2d353b", "#000000" },
};
/* -l option; if nonzero, dmenu uses vertical list with given number of lines */
static unsigned int lines      = 0;

/*
 * Characters not considered part of a word while deleting words
 * for example: " /?\"&[]"
 */
static const char worddelimiters[] = " ";

/* Size of the window border */
static const unsigned int border_width = 4;

/* -h option; minimum height of a menu line */
static unsigned int lineheight = 0;
static unsigned int min_lineheight = 8;
