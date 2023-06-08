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
```

| Input                 | Output               |
| --------------------- | -------------------- |
| APL                   |                      |
| Assembly              |                      |
| Bash/Shell            | x                    |
| Bash/Shell/PowerShell | x                    |
| C                     |                      |
| C#                    |                      |
| C++                   |                      |
| COBOL                 | Cobol                |
| CSS                   |                      |
| Clojure               |                      |
| Cobol                 |                      |
| CoffeeScript          |                      |
| Common Lisp           |                      |
| Crystal               |                      |
| Dart                  |                      |
| Delphi                | Delphi/Object Pascal |
| Delphi/Object Pascal  | x                    |
| Elixir                |                      |
| Erlang                |                      |
| F#                    |                      |
| Fortran               |                      |
| Go                    |                      |
| Groovy                |                      |
| HTML                  | x                    |
| HTML/CSS              | x                    |
| Hack                  |                      |
| Haskell               |                      |
| Java                  |                      |
| JavaScript            |                      |
| Julia                 |                      |
| Kotlin                |                      |
| LISP                  |                      |
| Lua                   |                      |
| MATLAB                | Matlab               |
| Matlab                |                      |
| Node.js               |                      |
| OCaml                 | Ocaml                |
| Objective-C           |                      |
| Ocaml                 |                      |
| Other(s):             | x                    |
| PHP                   |                      |
| Perl                  |                      |
| PowerShell            | x                    |
| Python                |                      |
| R                     |                      |
| Ruby                  |                      |
| Rust                  |                      |
| SAS                   |                      |
| SQL                   |                      |
| Scala                 |                      |
| Smalltalk             |                      |
| Solidity              |                      |
| Swift                 |                      |
| TypeScript            |                      |
| VB.NET                |                      |
| VBA                   | VB.NET               |
| Visual Basic 6        |                      |
| WebAssembly           |                      |

## Process

###
