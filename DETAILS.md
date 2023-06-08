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

-   Those marked `x` are removed from dataset because they appear in different combinations (like Bash, Bash/Shell, Bash/Shell/PowerShell, PowerShell) over years.
-   Those marked `m` are removed from dataset because they don't have data for each year.
-   Some of the languages appear with different capitalizations (like COBOL, Cobol). Those are firstly translated into one. But eventually got removed from dataset because they also suffer problems above.

| Input                 | Output               |
| --------------------- | -------------------- |
| APL                   | m                    |
| Assembly              |                      |
| Bash/Shell            | x                    |
| Bash/Shell/PowerShell | x                    |
| C                     |                      |
| C#                    |                      |
| C++                   |                      |
| Clojure               | m                    |
| COBOL                 | Cobol                |
| Cobol                 | m                    |
| CoffeeScript          | m                    |
| Common Lisp           | m                    |
| Crystal               | m                    |
| CSS                   | x                    |
| Dart                  | m                    |
| Delphi                | Delphi/Object Pascal |
| Delphi/Object Pascal  | m                    |
| Elixir                | m                    |
| Erlang                | m                    |
| F#                    | m                    |
| Fortran               | m                    |
| Go                    |                      |
| Groovy                | m                    |
| Hack                  | m                    |
| Haskell               | m                    |
| HTML                  | x                    |
| HTML/CSS              | x                    |
| Java                  |                      |
| JavaScript            |                      |
| Julia                 | m                    |
| Kotlin                | m                    |
| LISP                  | m                    |
| Lua                   | m                    |
| Matlab                | m                    |
| MATLAB                | Matlab               |
| Node.js               | m                    |
| Objective-C           |                      |
| Ocaml                 |                      |
| Ocaml                 | m                    |
| OCaml                 | Ocaml                |
| Other(s):             | x                    |
| Perl                  | m                    |
| PHP                   |                      |
| PowerShell            | x                    |
| Python                |                      |
| R                     |                      |
| Ruby                  |                      |
| Rust                  |                      |
| SAS                   | m                    |
| Scala                 |                      |
| Smalltalk             | m                    |
| Solidity              | m                    |
| SQL                   |                      |
| Swift                 |                      |
| TypeScript            |                      |
| VB.NET                | m                    |
| VBA                   | VB.NET               |
| Visual Basic 6        | m                    |
| WebAssembly           | m                    |

## Process

###
