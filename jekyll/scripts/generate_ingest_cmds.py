# Path to files
path = "../../RawDocx/20250323/"

# To get filenames run this in directory with files
#  % for x in *; do echo \"$x\"\,; done | xargs -0
files = [
    "CBF #401; June 8, 1949.docx",
    "CBF #402; June 10, 1949.docx",
    "CBF #403; June 13, 1949.docx",
    "CBF #404; June 14, 1949.docx",
    "CBF #405; June 15, 1949.docx",
    "CBF #406; June 16, 1949.docx",
    "CBF #407; June 17, 1949.docx",
    "CBF #408; June 20, 1949.docx",
    "CBF #409; June 21, 1949.docx",
    "CBF #410; June 22, 1949.docx",
    "CBF #411; June 23, 1949.docx",
    "CBF #412; June 24, 1949.docx",
    "CBF #413; June 27, 1949.docx",
    "CBF #414; June, 28, 1949.docx",
    "CBF #415; June 29, 1949.docx",
    "CBF #416; June 30, 1949.docx",
    "CBF #417; July 1, 1949.docx",
    "CBF #418; July 4, 1949.docx",
    "CBF #419; July 5, 1949.docx",
    "CBF #420; July 6, 1949.docx",
    "CBF #421; July 7, 1949.docx",
    "CBF #422; July 8, 1949.docx",
    "CBF #423; July 11, 1949.docx",
    "CBF #424; July 12, 1949.docx",
    "CBF #425; July 13, 1949.docx",
    "CBF #426; July 14, 1949.docx",
    "CBF #427; July 15, 1949.docx",
    "CBF #428; July 18, 1949.docx",
    "CBF #429; July 19, 1949.docx",
    "CBF #430; July 20, 1949.docx",
    "CBF #431; July 21, 1949.docx",
    "CBF #432; July 22, 1949.docx",
    "CBF #433; July 25, 1949.docx",
    "CBF #434; July 26, 1949.docx",
    "CBF #435; July 27, 1949.docx",
    "CBF #436; July 28, 1949.docx",
    "CBF #437; July 29, 1949.docx",
    "CBF #438; Aug. 1, 1949.docx",
    "CBF #439; Aug. 2, 1949.docx",
    "CBF #440; Aug. 3, 1949.docx",
    "CBF #441; Aug. 4, 1949.docx",
    "CBF #442; Aug. 5, 1949.docx",
    "CBF #443; Aug. 8, 1949.docx",
    "CBF #444; Aug. 9, 1949.docx",
    "CBF #445; Aug. 10, 1949.docx",
    "CBF #446; Aug. 11, 1949.docx",
    "CBF #447; Aug. 12, 1949.docx",
    "CBF #448; Aug. 15, 1949.docx",
    "CBF #449; Aug. 16, 1949.docx",
    "CBF #450; Aug. 17, 1949.docx",
    "CBF #451; Aug. 18, 1949.docx",
    "CBF #452; Aug. 19, 1949.docx",
    "CBF #453; Aug. 22, 1949.docx",
    "CBF #454; Aug. 23, 1949.docx",
    "CBF #455; Aug. 24, 1949.docx",
    "CBF #456; Aug. 25, 1949.docx",
    "CBF #457; Aug. 26, 1949.docx",
    "CBF #458; Aug. 29, 1949.docx",
    "CBF #459; Aug. 30, 1949.docx",
    "CBF #460; Aug. 31, 1949.docx",
    "CBF #461; Sept. 1, 1949.docx",
    "CBF #462; Sept. 2, 1949.docx",
    "CBF #463; Sept. 5, 1949.docx",
    "CBF #464; Sept. 6, 1949.docx",
    "CBF #465; Sept. 7, 1949.docx",
    "CBF #466; Sept. 8, 1949.docx",
    "CBF #467; Sept. 9, 1949.docx",
    "CBF #468; Sept. 12, 1949.docx",
    "CBF #469; Sept. 13, 1949.docx",
    "CBF #470; Sept. 14, 1949.docx",
    "CBF #471; Sept. 15, 1949.docx",
    "CBF #472; Sept. 16, 1949.docx",
    "CBF #473; Sept. 19, 1949.docx",
    "CBF #474; Sept. 20, 1949.docx",
    "CBF #475; Sept. 21, 1949.docx",
    "CBF #476; Sept. 22, 1949.docx",
    "CBF #477; Sept. 23, 1949.docx",
    "CBF #478; Sept. 26, 1949.docx",
    "CBF #479; Sept. 27, 1949.docx",
    "CBF #480; Sept. 28, 1949.docx",
    "CBF #481; Sept. 29, 1949.docx",
    "CBF #482; Sept. 30, 1949.docx",
    "CBF #483; Oct. 1, 1949.docx",
    "CBF #484; Oct. 3, 1949.docx",
    "CBF #485; Oct. 4, 1949.docx",
    "CBF #486; Oct. 5, 1949.docx",
    "CBF #487; Oct. 6, 1949.docx",
    "CBF #488; Oct. 7, 1949.docx",
    "CBF #489; Oct. 10, 1949.docx",
    "CBF #490; Oct. 11, 1949.docx",
    "CBF #491; Oct. 12, 1949.docx",
    "CBF #492; Oct. 13, 1949.docx",
    "CBF #493; Oct. 14, 1949.docx",
    "CBF #494; Oct. 17, 1949.docx",
    "CBF #495; Oct. 18, 1949.docx",
    "CBF #496; Oct. 19, 1949.docx",
    "CBF #497; Oct. 20, 1949.docx",
    "CBF #498; Oct. 21, 1949.docx",
    "CBF #499; Oct. 24, 1949.docx",
    "CBF #500; Oct. 25, 1949.docx",
    "CBF #501; Oct. 26, 1949.docx",
    "CBF #502; Oct. 27, 1949.docx",
    "CBF #503; Oct. 28, 1949.docx",
    "CBF #504; Oct. 31, 1949.docx",
    "CBF #505; Nov. 1, 1949.docx",
    "CBF #506; Nov. 2, 1949.docx",
    "CBF #507; Nov. 3, 1949.docx",
    "CBF #508; Nov. 4, 1949.docx",
    "CBF #509; Nov. 7, 1949.docx",
    "CBF #510; Nov. 8, 1949.docx",
    "CBF #511; Nov. 9, 1949.docx",
    "CBF #512; Nov. 10, 1949.docx",
    "CBF #513; Nov. 11, 1949.docx",
    "CBF #514; Nov. 14, 1949.docx",
    "CBF #515; Nov. 15, 1949.docx",
    "CBF #516; Nov. 16, 1949.docx",
    "CBF #517; Nov. 17, 1949.docx",
    "CBF #518; Nov. 18, 1949.docx",
    "CBF #519; Nov. 21, 1949.docx",
    "CBF #520; Nov. 22, 1949.docx",
    "CBF #521; Nov. 23, 1949.docx",
    "CBF #522; Nov. 24, 1949.docx",
    "CBF #523; Nov. 25, 1949.docx",
    "CBF #524; Nov. 28, 1949.docx",
    "CBF #525; Nov. 29, 1949.docx",
    "CBF #526; Nov. 30, 1949.docx",
    "CBF #527; Dec. 1, 1949.docx",
    "CBF #528; Dec. 2, 1949.docx",
    "CBF #529; Dec. 5, 1949.docx",
    "CBF #530; Dec. 6, 1949.docx",
    "CBF #531; Dec. 7, 1949.docx",
    "CBF #532; Dec. 8, 1949.docx",
    "CBF #533; Dec. 9, 1949.docx",
    "CBF #534; Dec. 12, 1949.docx",
    "CBF #535; Dec. 13, 1949.docx",
    "CBF #536; Dec. 14, 1949.docx",
    "CBF #537; Dec. 15, 1949.docx",
    "CBF #538; Dec. 16, 1949.docx",
    "CBF #539; Dec. 19, 1949.docx",
    "CBF #540; Dec. 20, 1949.docx",
    "CBF #541; Dec. 21, 1949.docx",
    "CBF #542; Dec. 22, 1949.docx",
    "CBF #543; Dec. 23, 1949.docx",
    "CBF #544; Dec. 26, 1949.docx",
    "CBF #545; Dec. 27, 1949.docx",
    "CBF #546; Dec. 28, 1949.docx",
    "CBF #547; Dec. 29, 1949.docx",
    "CBF #548; Dec. 30, 1949.docx",
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
