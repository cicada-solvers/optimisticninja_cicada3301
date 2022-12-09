#!/usr/bin/env bash

find . -type f -name "**.md" > mdfiles

if ![ -x "$(command -v npm)" ]; then
	echo "ERROR: Must have NPM installed."
	exit 1
fi

if ![ -x "$(command -v markdownlint)" ]; then
	npm install -g markdownlint-cli
fi

if ![ -x "$(command -v markdown-link-check)" ]; then
	npm install -g markdown-link-check
fi

find . -type f -name "*.md" | xargs -I % -t markdown-link-check % && markdownlint .

