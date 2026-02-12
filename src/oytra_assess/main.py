from oytra_assess.utils import process_signups

def main():
    process_signups(
        "data/raw/signup.xls",
        "data/processed/validmembers.csv",
        "data/processed/quarantine.csv",
    )

if __name__ == "__main__":
    main()
