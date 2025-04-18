from pathlib import Path

primer_trimestre = Path("datasets") / "1erTrimestre"
primer_hogar = primer_trimestre / "usu_hogar_T124.txt"
primer_individual = primer_trimestre / "usu_individual_T124.txt"

segundo_trimestre = Path("datasets") / "2doTrimestre"
segundo_hogar = segundo_trimestre / "usu_hogar_T224.txt"
segundo_individual = segundo_trimestre / "usu_individual_T224.txt"

tercer_trimestre = Path("datasets") / "3erTrimestre"
tercer_hogar = tercer_trimestre / "usu_hogar_T324.txt"
tercer_individual = tercer_trimestre / "usu_individual_T324.txt"

trimestres = Path("datasets") / "Trimestres"
trimestres_hogar = trimestres / "usu_hogar.txt"
trimestres_individual = trimestres / "usu_individual.txt"