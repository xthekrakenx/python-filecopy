## About python-filecopy

This simple script copies a file from one network location to another.


## Why This Tool Exists

My use case was that my wife has a network based spreadsheet that she relies on very heavily for running her business. She ran into an issue where it would have been nice to have a prior day's backup copy (without an elaborate system of course) but was complex enough that the process would run automatically without any human intervention. I decided to use python given how much you can accomplish with so few lines of code.

## Suggested Use/Pairing

While the script can be run on an as needed basis - it is really impactful as a scheduled task. I current have it implemented as a nightly task running at 12AM on my home theatre PC. To set it up as a scheduled task - you would map the scheduled task to your installed python.exe and pass the absolute file path to your script file in double quotes "C:\path\to\script.py" as an optional argument.

## Bugs

If you discover any bugs or have any tweaks you would like to share - please do not hesitate to forward those on to me: kraken@mykraken.tech.

## License

The python-filecopy is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
