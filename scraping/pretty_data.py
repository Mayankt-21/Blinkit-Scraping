import json
import pandas as pd
import datetime

# Desired fields:
# date, l1_category ,l1_category_id ,l2_category ,l2_category_id ,store_id ,variant_id ,variant_name ,group_id ,selling_price ,mrp ,in_stock ,inventory ,is_sponsored ,image_url ,brand_id ,brand

def pretty_data(response, l0_cat,l0_cat_id, l1_cat,l1_cat_id,lat,lon):
    
    data = response
    snippets_array = data["response"]["snippets"]
    
    all_records = []

    for snippet in snippets_array:
        d = snippet.get("data", {})
        atc_action = d.get("atc_action",{}).get("add_to_cart",{}).get("cart_item",{})
        record = {
            "date":datetime.datetime.now(),
            "l1_category":l0_cat,
            "l1_category_id":l0_cat_id,
            "l2_category":l1_cat,
            "l2_category_id":l1_cat_id,
            "name":d.get("name").get("text"),
            "image_url": d.get("image").get("url"),
            "variant_name": d.get("name_text"),
            "in_stock": not d.get("is_sold_out"),
            "group_id": d.get("group_id"),
            "store_id": d.get("merchant_id"),
            "variant_id": d.get("product_id"),
            "brand": d.get("brand_name",{}).get("text"),
            "inventory": d.get("inventory"),
            "mrp": atc_action.get("mrp"),
            "selling_price": d.get("normal_price",{}).get("text"),
            "brand_id": None,          # Not found in JSON
            "is_sponsored": None,      # Not found in JSON
        }

        
        variant_list = d.get("variant_list", [])
        variant_names=[]
        variant_id=[]
        for v in variant_list:
            variant_names.append(v["data"]["name"]["text"])
            variant_id.append(v["data"]["identity"]["id"])
            
        record["variant_name"] = ",".join(variant_names)
        record["variant_id"] = ",".join(variant_id)

        all_records.append(record)

    df = pd.DataFrame(all_records)

    # Save to CSV
    # df.to_csv("filtered_output.csv", index=False)
    # print("Saved filtered_output.csv with columns:\n", df.columns.to_list())
    return df
