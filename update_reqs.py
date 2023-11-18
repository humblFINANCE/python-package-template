import subprocess

from humbldata.core.helpers import MessageHelpers

msg = MessageHelpers.log_message

# Export Conda environment to environment.yml
subprocess.run(
    """conda env export | python -c "import sys; print(''.join(line for line in sys.stdin if 'prefix: ' not in line))" > environment.yml""",
    shell=True,
    check=True,
)

msg(
    "Updated [bright_yellow]environment.yml[/bright_yellow] [green3]" "successfully[/green3].",
    "success",
)

subprocess.run("conda list --export > requirements.txt", shell=True, check=True)
msg(
    "Updated [bright_yellow]requirements.txt[/bright_yellow] [green3]" "successfully[/green3].",
    "success",
)


# subprocess.run(
#     "poetry export --output requirements.txt", shell=True, check=True
# )
# msg(
#     "Updated [bright_yellow]requirements.txt[/bright_yellow] [green3]"
#     "successfully[/green3].",
#     "success",
# )
