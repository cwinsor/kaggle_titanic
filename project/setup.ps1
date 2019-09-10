
$TB_ROOT    = $PSScriptRoot
$TB_SCRIPTS = $PSScriptRoot

# if the virtualenv (pymote_env) does not exist then create it
# required libraries are identified in requirements.txt

if (-not (Test-Path "$TB_ROOT\pymote_env\Scripts\activate" -PathType Leaf)) {
    &"$TB_SCRIPTS\setup_onetime_00_restore_libraries.ps1"
    }

.\setup_everytime_00_activate_env.ps1
.\setup_everytime_01_add_cwd_to_path.ps1
.\setup_everytime_02_start_jupyter_notebook
#.\setup_everytime_03_start_code.ps1
