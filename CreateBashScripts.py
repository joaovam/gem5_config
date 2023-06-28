cap_programs = ["fn.intel",  "gf.intel" , "is.intel",  "km.intel",
                "lu.intel" , "nb.intel" , "rt.intel",  "tsp.intel"]
TOTAL_CORES = 24

cap_classes = ["tiny", "small", "standard", "large", "huge"]

for p in cap_programs:
    for core in range(1, TOTAL_CORES + 1, 1):
        for c in cap_classes:
            command = f"/CAPBENCH/{p} --nthread {core} --class {c}"
            print(command)
            with open(f"{p}_{c}_{core}", "w") as file:
                file.write(command + '\n')
                file.flush()