# Copia as skills deste repositorio para ~\.claude\skills\
$dest = Join-Path $HOME ".claude\skills"
$src  = Join-Path $PSScriptRoot "skills"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Write-Host "Instalando em $dest"
Get-ChildItem -Path $src -Directory | ForEach-Object {
  $alvo = Join-Path $dest $_.Name
  if (Test-Path $alvo) { Remove-Item -Recurse -Force $alvo }
  Copy-Item -Recurse $_.FullName $alvo
  Write-Host "  ok  $($_.Name)"
}
Write-Host ""
Write-Host "Feito. Fecha e abre o Claude Code, e pergunta: que skills voce tem disponiveis?"
