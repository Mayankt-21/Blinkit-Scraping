from my_scrapper import my_scrapper
from data import loadData
import pandas as pd

def main():
    cats, locs = loadData()
    all_dfs = []
    delay=30
    
    # print(locs)
    # print(cats)
    for cat in cats:
        l0_cat = cat[0]
        l0_cat_id = cat[1]
        l1_cat = cat[2]
        l1_cat_id = cat[3]

        for loc in locs:
            lat = (loc[0].strip('"'))
            lon = (loc[1].strip('"'))

            print(f"Scraping => {l0_cat} > {l1_cat} at [{lat}, {lon}]")
            df = my_scrapper(lat, lon, l0_cat, l0_cat_id, l1_cat, l1_cat_id,delay)
            if df is not None and not df.empty:
                all_dfs.append(df)

    # Final merged output
    final_df = pd.concat(all_dfs, ignore_index=True)
    final_df.to_csv("final_output.csv", index=False)
    print("Saved final_output.csv with", len(final_df), "rows.")




if __name__ == "__main__":
    main()