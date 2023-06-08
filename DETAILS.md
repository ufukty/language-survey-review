## Dataset

https://insights.stackoverflow.com/survey

## Clearing

### Column matching

Since there are more than one schema used over years, each required different method to clear. Table shows which columns used from dataset of each year to get `Languages want to work` and `Languages used`. Sharps are for column indexes.

| Year | "Have"                 | #   | "Want"                 | #   |
| ---- | ---------------------- | --- | ---------------------- | --- |
| 2017 | HaveWorkedLanguage     | 88  | WantWorkLanguage       | 89  |
| 2018 | LanguageWorkedWith     | 65  | LanguageDesireNextYear | 66  |
| 2019 | LanguageWorkedWith     | 43  | LanguageDesireNextYear | 44  |
| 2020 | LanguageWorkedWith     | 22  | LanguageDesireNextYear | 21  |
| 2021 | LanguageHaveWorkedWith | 16  | LanguageWantToWorkWith | 17  |
| 2022 | LanguageHaveWorkedWith | 19  | LanguageWantToWorkWith | 20  |

### Listing all languages

Languages that not shown below are ignored.

```sh
$ find clean -type f | while read FILE; do
    cat "$FILE" | jq -r '.[] | to_entries[] | .key';
done | sort | uniq > all_langs.txt

$ cat all_langs.txt
APL
Assembly
Bash/Shell
Bash/Shell/PowerShell
C
C#
C++
COBOL
CSS
Clojure
Cobol
CoffeeScript
Common Lisp
Crystal
Dart
Delphi
Delphi/Object Pascal
Elixir
Erlang
F#
Fortran
Go
Groovy
HTML
HTML/CSS
Hack
Haskell
Java
JavaScript
Julia
Kotlin
LISP
Lua
MATLAB
Matlab
Node.js
OCaml
Objective-C
Ocaml
Other(s):
PHP
Perl
PowerShell
Python
R
Ruby
Rust
SAS
SQL
Scala
Smalltalk
Solidity
Swift
TypeScript
VB.NET
VBA
Visual Basic 6
WebAssembly
```
