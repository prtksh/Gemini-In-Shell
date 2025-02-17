# Gemini-In-Shell

A Python script that you can download and run in your terminal to access Gemini (model: 1.5-Pro on the free tier), for a chat or query. Only textual content to-and-fro (for now). 

> [!NOTE]
> This project is made as a practice / side project. Though this holds no greater influence, any suggestions or advice or issues sent about the workings, logic, build or etc is greatly appreciated !

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
  * [Interactive](#interactive)
  * [Inline](#inline)
* [Dependencies](#dependencies)
* [License](#license)

> [!IMPORTANT]  
> This project is made to run on Linux systems. You need to have a GEMINI-API-KEY already in your environment (or .bashrc) file for you to connect to Gemini.

## Installation
To install this package:

```bash
pip install gemini-in-shell==0.1.0
```

## Usage
There are two ways to use this package

### Interactive
```bash
shell-gemini --interactive
```
This starts a conversation with Gemini in your terminal with multiple queries one after the other. No need to re-run the package everytime.

### Inline
```bash
shell-gemini "<query>"
```
A simpler option if you want a response for just one query without the hassle of having to exit the interactive mode.

## Dependencies
* Google GenerativeAI (google.generativeai) - For connecting with Gemini and receiving responses to-and-fro. Needs a GEMINI_API_KEY to function and connect.
* argparse (argparse) - To take the command line query inputs and setup the modes.
* grpcio (grpcio) - To eliminate the error messages that would be printed in / after Gemini's responses. Version 1.60.0 is the closest and latest version I could find that would allow this.
* os (os) - Built-in in most Python environments, used to check if the user's .bashrc file has the GEMINI_API_KEY in it for the program to run.

## License
This project is under the MIT License. Check LICENSE for more details.







