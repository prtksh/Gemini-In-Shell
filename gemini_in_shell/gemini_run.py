# Copyright (c) 2025 Pratiksha Naik
#!/usr/bin/env python3

import google.generativeai as genai
import argparse
import os
os.environ["GRPC_VERBOSITY"] = "ERROR"


apiKey = os.getenv("GEMINI_API_KEY")
if not apiKey:
    raise ValueError("No Gemini API key found! Please make sure you have it on your environment / system!")

genai.configure(api_key=apiKey)

def gemini_query(question):
    model = genai.GenerativeModel("gemini-1.5-pro") 
    response = model.generate_content(
            question)
    return response.text

def main():
    parser = argparse.ArgumentParser(description="Query Gemini")
    parser.add_argument("question", nargs="?", help="Ask Gemini a question directly while calling it without interactive mode.")
    parser.add_argument("--interactive",action="store_true",help="Converse with Gemini in interactive mode without having to rerun the package")

    args = parser.parse_args()

    if args.question:
        print(gemini_query(args.question))
    elif args.interactive:
        print("You are talking to Gemini ! Enter 'bye' to exit")
        while True:
            query = input(">> ")
            if query=="bye":
                print("BYE!")
                break
    
            print("________\n")
            print(gemini_query(query))
            print("________\n")
    else:
        print("Enter a question, or use --interactive mode, or display help")


