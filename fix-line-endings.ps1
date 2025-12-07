$files = @('about.html', 'index.html')
foreach ($file in $files) {
    $content = Get-Content $file -Raw
    $content = $content -replace "`r`n", "`n"
    $content = $content -replace "`n", "`r`n"
    [System.IO.File]::WriteAllText((Resolve-Path $file), $content)
}
Write-Host "Line endings fixed"
