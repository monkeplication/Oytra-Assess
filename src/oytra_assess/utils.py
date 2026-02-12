import pandas as pd
import re
#Breaking each step into a function for better readability and to not cause a mess

def normalize_email(email):
    # Normalizes an email address by:
    # converting to lowercase, stripping whitespace, removing anything after + in gmail addresses cause it doesnt matter
    email = str(email).strip().lower()
    if "@gmail.com" in email:
        email = re.sub(r"\+.*(?=@gmail\.com)", "", email)
    return email

def is_low_quality(row):
    # checks if a row is spam based on namw and email
    name = str(row["name"]).lower()
    email = str(row["email"]).lower()

    if "test" in name:
        return True
    if re.search(r"[^a-zA-Z ]", name):
        return True
    if "test@" in email:
        return True
    return False

def process_signups(input_path, final_path, quarantine_path):
    # processes the signups.xls
    df_raw = pd.read_excel(input_path, engine="xlrd")

    df_split = df_raw.iloc[:, 0].astype(str).str.split(",", n=4, expand=True)
    df_split.columns = ["name", "email", "signup_date", "plan", "notes"]

    df = df_split.copy()
    # normalizing email
    df["email"] = df["email"].apply(normalize_email)
    # converting signup date to datetime
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
    # checking for low quality rows
    quarantine_mask = df.apply(is_low_quality, axis=1) | df["signup_date"].isna()
    quarantine_df = df_raw.iloc[quarantine_mask.values].copy()
    clean_df = df[~quarantine_mask].copy()
    # sorting by signup date
    clean_df = clean_df.sort_values("signup_date")
    # checking for multi plan
    multi_plan = clean_df.groupby("email")["plan"].nunique() > 1
    multi_plan = multi_plan.to_dict()
    clean_df = clean_df.drop_duplicates(subset=["email"], keep="last")
    # adding the multi plan column
    clean_df["is_multi_plan"] = clean_df["email"].map(multi_plan).fillna(False)
    clean_df["signup_date"] = clean_df["signup_date"].dt.strftime("%Y-%m-%d")
    clean_df.to_csv(final_path, index=False)
    quarantine_df.to_csv(quarantine_path, index=False)
