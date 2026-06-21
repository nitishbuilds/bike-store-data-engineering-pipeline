import subprocess
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_step(step_name, command):
    print(f"\n{'='*50}")
    print(f"RUNNING: {step_name}")
    print(f"{'='*50}")

    logging.info(f"STARTED: {step_name}")

    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        logging.error(f"FAILED: {step_name}")
        print(f"FAILED: {step_name}")
        exit(1)

    logging.info(f"SUCCESS: {step_name}")
    print(f"SUCCESS: {step_name}")


if __name__ == "__main__":

    logging.info("PIPELINE STARTED")

    run_step(
        "Create Schemas and Tables",
        "python3 -m load.run_sql"
    )

    run_step(
        "Load Staging Data",
        "python3 -m load.load_staging"
    )

    run_step(
        "Validate Data",
        "python3 -m validate.validate"
    )

    run_step(
        "Load Dimensions",
        "python3 -m transform.load_dimensions"
    )

    run_step(
        "Load Date Dimension",
        "python3 -m transform.load_dim_date"
    )

    run_step(
        "Load Fact Sales",
        "python3 -m transform.load_fact_sales"
    )

    run_step(
        "Load Fact Inventory",
        "python3 -m transform.load_fact_inventory"
    )

    logging.info("PIPELINE COMPLETED SUCCESSFULLY")

    print("\nPIPELINE COMPLETED SUCCESSFULLY")
