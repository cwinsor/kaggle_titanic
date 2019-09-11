
# add current directory to PATH (so libraries can be found)

$Env:PYTHONPATH=''
$Env:PYTHONPATH="$ENV:PYTHONPATH$PSScriptRoot;"
$Env:PYTHONPATH="$ENV:PYTHONPATH$PSScriptRoot/lib;"
$Env:PYTHONPATH="$ENV:PYTHONPATH$PSScriptRoot/lib/python-id3-cwinsor;"
$Env:PYTHONPATH="$ENV:PYTHONPATH$PSScriptRoot/lib/python-id3-trees;"


