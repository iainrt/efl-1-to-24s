from dotenv import load_dotenv
load_dotenv()  # take environment variables
from efl_1_to_24s.supabase import supabase


def main():
    print("Hello from efl-1-to-24s!")
    response = (
        supabase.table("test")
        .select("*")
        .execute()
    )
    print(response.data)

if __name__ == "__main__":
    main()
