#!/usr/bin/env bash
# Copia as skills deste repositório para ~/.claude/skills/
set -e
DEST="$HOME/.claude/skills"
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"
mkdir -p "$DEST"
echo "Instalando em $DEST"
for d in "$SRC"/*/; do
  nome="$(basename "$d")"
  rm -rf "$DEST/$nome"
  cp -r "$d" "$DEST/$nome"
  echo "  ok  $nome"
done
echo
echo "Feito. Fecha e abre o Claude Code, e pergunta: que skills você tem disponíveis?"
