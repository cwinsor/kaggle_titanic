
# add current directory to PATH (so libraries can be found)

$Env:PYTHONPATH=$ENV:PYTHONPATH + $PSScriptRoot
$Env:PYTHONPATH=$ENV:PYTHONPATH + ';'

$Env:PYTHONPATH=$ENV:PYTHONPATH + $PSScriptRoot
$Env:PYTHONPATH=$ENV:PYTHONPATH + '/lib;'
