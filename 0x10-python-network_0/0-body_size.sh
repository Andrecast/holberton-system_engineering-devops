#!/bin/bash
#s: silent, no muestra el progress o error messages, I head info, d: delimiter, f: only these fields
curl -sI "$1" | grep Content-Length | cut -d" " -f2
