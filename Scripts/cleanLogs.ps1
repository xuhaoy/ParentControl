﻿Get-ChildItem "C:\ParentControl\logs\" -Recurse -File | Where CreationTime -lt  (Get-Date).AddDays(-2)  | Remove-Item -Force