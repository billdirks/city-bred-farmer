# Path to files
path = "../../RawDocx/20250322/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #313; Feb. 7, 1949.docx",
    "CBF #314; Feb. 8, 1949.docx",
    "CBF #315; Feb. 9, 1949.docx",
    "CBF #316; Feb. 10, 1949.docx",
    "CBF #317; Feb. 11, 1949.docx",
    "CBF #318; Feb. 14, 1949.docx",
    "CBF #319; Feb. 15, 1949.docx",
    "CBF #320; Feb. 16, 1949.docx",
    "CBF #321; Feb. 17, 1949.docx",
    "CBF #322; Feb. 18, 1949.docx",
    "CBF #323; Feb. 21, 1949.docx",
    "CBF #324; Feb. 22, 1949.docx",
    "CBF #325; Feb. 23, 1949.docx",
    "CBF #326; Feb. 24, 1949.docx",
    "CBF #327; Feb. 25, 1949.docx",
    "CBF #328; Feb. 28, 1949.docx",
    "CBF #329; March 1, 1949.docx",
    "CBF #330; March 2, 1949.docx",
    "CBF #331; March 3, 1949.docx",
    "CBF #332; March 4, 1949.docx",
    "CBF #333; March 7, 1949.docx",
    "CBF #334; March 8, 1949.docx",
    "CBF #335; March 9, 1949.docx",
    "CBF #336; March 10, 1949.docx",
    "CBF #337; March 11, 1949.docx",
    "CBF #338; March 14, 1949.docx",
    "CBF #339; March 15, 1949.docx",
    "CBF #340; March 16, 1949.docx",
    "CBF #341; March 17, 1949.docx",
    "CBF #342; March 18, 1949.docx",
    "CBF #343; March 21, 1949.docx",
    "CBF #344; March 22, 1949.docx",
    "CBF #345; March 23, 1949.docx",
    "CBF #346; March 24, 1949.docx",
    "CBF #347; March 25, 1949.docx",
    "CBF #348; March 28, 1949.docx",
    "CBF #349; March 29, 1949.docx",
    "CBF #350; March 30, 1949.docx",
    "CBF #351; March 31, 1949.docx",
    "CBF #352; April 1, 1949.docx",
    "CBF #353; April 4, 1949.docx",
    "CBF #354; April 5, 1949.docx",
    "CBF #355; April 6, 1949.docx",
    "CBF #356; April 7, 1949.docx",
    "CBF #357; April 8, 1949.docx",
    "CBF #358; April 11, 1949.docx",
    "CBF #359; April 12, 1949.docx",
    "CBF #360; April 13, 1949.docx",
    "CBF #361; April 14, 1949.docx",
    "CBF #362; April 15, 1949.docx",
    "CBF #363; April 18, 1949.docx",
    "CBF #364; April 19, 1949.docx",
    "CBF #365; April 20, 1949.docx",
    "CBF #366; April 21, 1949.docx",
    "CBF #367; April 22, 1949.docx",
    "CBF #368; April 25, 1949.docx",
    "CBF #369; April 26, 1949.docx",
    "CBF #370; April 27, 1949.docx",
    "CBF #371; April 28, 1949.docx",
    "CBF #372; April 29, 1949.docx",
    "CBF #373; May 2, 1949.docx",
    "CBF #374; May 3, 1949.docx",
    "CBF #375; May 4, 1949.docx",
    "CBF #376; May 5, 1949.docx",
    "CBF #377; May 6, 1949.docx",
    "CBF #378; May 9, 1949.docx",
    "CBF #379; May 10, 1949.docx",
    "CBF #380; May 11, 1949.docx",
    "CBF #381; May 12, 1949.docx",
    "CBF #382; May 13, 1949.docx",
    "CBF #383; May 16, 1949.docx",
    "CBF #384; May 17, 1949.docx",
    "CBF #385; May 18, 1949.docx",
    "CBF #386; May 19, 1949.docx",
    "CBF #387; May 20, 1949.docx",
    "CBF #388; May 23, 1949.docx",
    "CBF #389; May 24, 1949.docx",
    "CBF #390; May 25, 1949.docx",
    "CBF #391; May 26, 1949.docx",
    "CBF #392; May 27, 1949.docx",
    "CBF #393; May 30, 1949.docx",
    "CBF #394; May 31, 1949.docx",
    "CBF #395; June 1, 1949.docx",
    "CBF #396; June 2, 1949.docx",
    "CBF #397; June 3, 1949.docx",
    "CBF #398; June 6, 1949.docx",
    "CBF #399; June 7, 1949.docx",
    "CBF #400; June 8, 1949.docx",
]

def to_month(filename: str) -> str:
    fn = filename.casefold()
    if "jan" in fn:
        return "01"
    elif "feb" in fn:
        return "02"
    elif "mar" in fn:
        return "03"
    elif "apr" in fn:
        return "04"
    elif "may" in fn:
        return "05"
    elif "jun" in fn:
        return "06"
    elif "jul" in fn:
        return "07"
    elif "aug" in fn:
        return "08"
    elif "sep" in fn:
        return "09"
    elif "oct" in fn:
        return "10"
    elif "nov" in fn:
        return "11"
    elif "dec" in fn:
        return "12"
    raise Exception("no month found")

def parse_date(filename: str) -> tuple[str, str, str]:
    year = filename[-9:-5]
    day = filename[-13:-11]
    day = day if day[0] != " " else f"0{day[1]}"
    month = to_month(filename)
    return (year, str(month), day)

if __name__ == '__main__':
    for f in sorted(files, key=parse_date):
        year, month, day = parse_date(f)
        print(f'python3 ./ingest_docx.py --date {year}{month}{day} --docx "{path}{f}"')
