# ReAct: Reasoning and Acting in Language Models

A small Python implementation of the ReAct (Reasoning + Acting) prompting loop for question answering, with loaders for the HotpotQA and FEVER datasets.

## Overview

ReAct interleaves model reasoning ("thought") with tool use ("action") and the resulting "observation". This repository runs that thought-action-observation loop against an LLM served through the OpenRouter API and writes predictions per dataset to JSONL logs.

![ReAct overview](assets/react.png)

## Features

- ReAct agent loop with a configurable step limit (`agent.py`, default 5 steps)
- Prompt template enforcing the `Thought / Act / Observation` format (`prompts.py`)
- OpenRouter chat-completions client with retries (`llm_interface.py`)
- Dataset loaders for HotpotQA and FEVER (`environments/`)
- Batch runner that saves predictions to `data/logs/*.jsonl` (`main.py`)
- Simple accuracy script for scored logs (`evaluate_comparison.py`)

Note: the agent's `Search[...]` observations are currently mocked (`ReActAgent.mock_observe`), not retrieved from a real search tool.

## Project structure

```
.
├── agent.py                 # ReActAgent loop
├── llm_interface.py         # OpenRouter API client
├── prompts.py               # Prompt template
├── main.py                  # Run the agent over HotpotQA and FEVER
├── evaluate_comparison.py   # Accuracy over result logs
├── utils.py
├── environments/            # Dataset loaders (hotpotqa_env.py, fever_env.py)
├── data/                    # hotpotqa.json, fever.json
├── assets/                  # Images used in this README
└── requirements.txt
```

## Setup

Requires Python 3.8+ and an [OpenRouter](https://openrouter.ai) API key.

```bash
git clone https://github.com/m0han-raj/ReAct-reasoning-and-acting.git
cd ReAct-reasoning-and-acting
pip install -r requirements.txt
```

Create a `.env` file in the repository root:

```
OPENROUTER_API_KEY=<your_api_key>
```

The model is set in `llm_interface.py`.

## Usage

```bash
python main.py
```

This runs the agent on samples from `data/hotpotqa.json` and `data/fever.json` and writes `data/logs/hotpotqa_results.jsonl` and `data/logs/fever_results.jsonl`.

## Example output

The model responds in a thought / action format:

![Example output](assets/output.png)

## Tech stack

Python, `requests`, `python-dotenv`, OpenRouter API.

## References

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., Cao, Y. "ReAct: Synergizing Reasoning and Acting in Language Models." ICLR 2023. https://arxiv.org/abs/2210.03629

```bibtex
@inproceedings{yao2023react,
  title     = {{ReAct}: Synergizing Reasoning and Acting in Language Models},
  author    = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2023},
  url       = {https://arxiv.org/abs/2210.03629}
}
```

## License

MIT. See [LICENSE](LICENSE).
