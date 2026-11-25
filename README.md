# EnergoCore

Учебный прототип оптимизации энергопотребления кампуса. На вход подаётся готовый почасовой прогноз базовой нагрузки в кВт. Программа выбирает час для дополнительной нагрузки постоянной мощности, например зарядки оборудования, так, чтобы итоговый пик мощности был минимальным. При равенстве выбирается самый ранний час.

Запуск с Python 3, без внешних зависимостей:

```sh
python energocore.py --forecast 48 62 55 41 --load 15
```

В примере оптимален четвёртый час: при немедленном запуске пик составит 63 кВт, при переносе — 62 кВт. Нумерация часов начинается с единицы.

## Git на защите

Покажите опубликованную историю командой `git log --graph --oneline --all`.
Ветки `team-start`, `demo/revert` и `demo/cherry-pick` опубликованы в репозитории. Для повторения используйте свежий клон и локальные ветки.

Проверка игнорирования в PowerShell:

```powershell
[IO.File]::WriteAllBytes((Join-Path (Get-Location) 'probe.bin'), [byte[]](1,2,3))
git add -- probe.bin
git check-ignore -v probe.bin
git ls-files -- probe.bin
Remove-Item -LiteralPath probe.bin
```

Ожидается отказ от `git add`, совпадение с правилом `*.bin` и пустой вывод `git ls-files`.

Для командных PR каждый участник создаёт форк, создаёт рабочую ветку от актуальной `main` в форке и дописывает свою фамилию в `team.txt` отдельной строкой. PR направляется в `b450b/EnergoCore:main`. Открывайте PR по очереди, обновляя форк после каждого слияния. Пустой файл можно показать в ветке `team-start`.

Повторение отката и слияния:

```powershell
git switch -c rehearsal-main main
git switch -c rehearsal-revert origin/team-start
'Temporary text' | Set-Content -Encoding ascii team.txt
git add team.txt
git commit -m 'Write temporary text'
git revert --no-edit HEAD
git switch rehearsal-main
git merge --no-ff rehearsal-revert -m 'Merge revert rehearsal'
```

Повторение переноса второго из трёх коммитов:

```powershell
git switch -c rehearsal-pick rehearsal-main
foreach ($n in 1..3) {
    $file = "rehearsal-$n.txt"
    "Example $n" | Set-Content -Encoding ascii $file
    git add -- $file
    git commit -m "Add $file"
}
git switch rehearsal-main
git cherry-pick -x rehearsal-pick~1
git ls-files -- 'rehearsal-*.txt'
```

Последняя команда должна вывести только `rehearsal-2.txt`. На GitHub тот же результат виден в `main`, где из трёх демонстрационных файлов присутствует только `example-2.txt`.
