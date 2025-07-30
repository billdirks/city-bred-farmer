# Path to files
path = "../../RawDocx/20250730/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #510101.docx",
    "CBF #510102.docx",
    "CBF #510103.docx",
    "CBF #510105.docx",
    "CBF #510108.docx",
    "CBF #510109.docx",
    "CBF #510110.docx",
    "CBF #510112.docx",
    "CBF #510115.docx",
    "CBF #510117.docx",
    "CBF #510122.docx",
    "CBF #510124.docx",
    "CBF #510125.docx",
    "CBF #510126.docx",
    "CBF #510129.docx",
    "CBF #510201.docx",
    "CBF #510205.docx",
    "CBF #510206.docx",
    "CBF #510207.docx",
    "CBF #510208.docx",
    "CBF #510209.docx",
    "CBF #510213.docx",
    "CBF #510214.docx",
    "CBF #510215.docx",
    "CBF #510216.docx",
    "CBF #510222.docx",
    "CBF #510226.docx",
    "CBF #510227.docx",
    "CBF #510305.docx",
    "CBF #510306.docx",
    "CBF #510307.docx",
    "CBF #510309.docx",
    "CBF #510312.docx",
    "CBF #510313.docx",
    "CBF #510314.docx",
    "CBF #510316.docx",
    "CBF #510320.docx",
    "CBF #510321.docx",
    "CBF #510323.docx",
    "CBF #510326.docx",
    "CBF #510329.docx",
    "CBF #510330.docx",
    "CBF #510405.docx",
    "CBF #510406.docx",
    "CBF #510410.docx",
    "CBF #510503.docx",
    "CBF #510508.docx",
    "CBF #510509.docx",
    "CBF #510516.docx",
    "CBF #510528.docx",
    "CBF #510529.docx",
    "CBF #510530.docx",
    "CBF #510531.docx",
    "CBF #510702.docx",
    "CBF #510709.docx",
    "CBF #510712.docx",
    "CBF #510719.docx",
    "CBF #510723.docx",
    "CBF #510724.docx",
    "CBF #510725.docx",
    "CBF #510731.docx",
    "CBF #510802.docx",
    "CBF #510803.docx",
    "CBF #510807.docx",
    "CBF #510808.docx",
    "CBF #510810.docx",
    "CBF #510813.docx",
    "CBF #510815.docx",
    "CBF #510816.docx",
    "CBF #510821.docx",
    "CBF #510824.docx",
    "CBF #510829.docx",
    "CBF #510830.docx",
    "CBF #510905.docx",
    "CBF #510906.docx",
    "CBF #510911.docx",
    "CBF #510912.docx",
    "CBF #510925.docx",
    "CBF #510926.docx",
    "CBF #510927.docx",
    "CBF #511001.docx",
    "CBF #511003.docx",
    "CBF #511004.docx",
    "CBF #511005.docx",
    "CBF #511010.docx",
    "CBF #511023.docx",
    "CBF #511203.docx",
    "CBF #511211.docx",
    "CBF #511213.docx",
    "CBF #520131.docx",
    "CBF #520201.docx",
    "CBF #520221.docx",
    "CBF #520229.docx",
    "CBF #520407.docx",
    "CBF #520409.docx",
    "CBF #520416.docx",
    "CBF #520418.docx",
    "CBF #520421.docx",
    "CBF #520422.docx",
    "CBF #520429.docx",
    "CBF #520502.docx",
    "CBF #520513.docx",
    "CBF #520514.docx",
    "CBF #520516.docx",
    "CBF #520522.docx",
    "CBF #520527.docx",
    "CBF #520528.docx",
    "CBF #520603.docx",
    "CBF #520605.docx",
    "CBF #520623.docx",
    "CBF #520708.docx",
    "CBF #520724.docx",
    "CBF #520725.docx",
    "CBF #520916.docx",
    "CBF #520917.docx",
    "CBF #520926.docx",
    "CBF #520930.docx",
    "CBF #521002.docx",
    "CBF #521003.docx",
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
    # year = filename[-9:-5]
    # day = filename[-13:-11]
    # day = day if day[0] != " " else f"0{day[1]}"
    # month = to_month(filename)
    # return (year, str(month), day)
    # CBF #520221.docx
    year = filename[5:7]
    month = filename[7:9]
    day = filename[9:11]
    return (year, month, day)

if __name__ == '__main__':
    for f in sorted(files, key=parse_date):
        year, month, day = parse_date(f)
        print(f'python3 ./ingest_docx.py --date {year}{month}{day} --docx "{path}{f}"')
