from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("🚀 Starting ETL Pipeline...")

    print("📥 Extracting data...")
    raw_data = extract_data()
    print(f"✅ Extracted {len(raw_data)} records")

    print("🔧 Transforming data...")
    transformed_data = transform_data(raw_data)
    print(f"✅ Transformed {len(transformed_data)} records")

    print("💾 Loading data...")
    load_data(transformed_data)
    print("✅ Data successfully saved to data/processed/products.json")

    print("🎉 ETL Pipeline completed!")

if __name__ == "__main__":
    run_pipeline()
