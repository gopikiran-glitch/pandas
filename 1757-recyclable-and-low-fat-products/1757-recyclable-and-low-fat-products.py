import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats']=='y')&(products['recyclable']=='y')][['product_id']]