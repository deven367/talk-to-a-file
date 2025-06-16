# Home

This is a very simple utility script that I just created so that you could send the content of a pdf to an LLM and talk to it.

## instructions

To install the app, you just need to do,

```sh
pip install talk-to-a-file

# or

pip install git+https://github.com/deven367/talk-to-a-file
```

If you wish to develop/contribute to the project,

```sh
git clone https://github.com/deven367/talk-to-a-file
cd talk-to-a-file
pip install -e .
```

### prerequisites

To use this package, you need to use your own `ANTHROPIC_API_KEY`. Before using the CLI command, you need to set the environment variable. To do so,

```sh
export ANTHROPIC_API_KEY=<your-api-key>
```

## how it works

Once the package is installed, you can use the CLI command, `talk-to-a-file`,

The CLI has a required argument, `pdf`, which is the path to the pdf file that you want to read.

![alt text](cli.png)

Here is a small example, where I talk to the pdf file, `docs/tcm.pdf`,

![alt text](cli-example.png)

To quit the CLI, you can type `exit` or `quit`.

## how to contribute

Issues and PRs are welcome. If you have any suggestions or improvements, feel free to open an issue or a PR.
