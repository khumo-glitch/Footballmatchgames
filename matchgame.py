import sqlite3

# This Function will allow me to connect to my database
def connect_to_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

# user can retrieve coach information by name
def retrieve_coach_info(conn, coach_name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Coach WHERE FirstName=?", (coach_name,))
    coach_data = cursor.fetchone()
    cursor.close()
    return coach_data

#User can retrieve player information by player ID
def retrieve_player_info(conn, player_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Players WHERE player_id=?", (player_id,))
    player_data = cursor.fetchone()
    cursor.close()
    return player_data

# User retrieves game information by game ID
def retrieve_game_info(conn, game_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Game WHERE game_id=?", (game_id,))
    game_data = cursor.fetchone()
    cursor.close()
    return game_data

# User can update player information
def update_player_info(conn, player_id, new_number):
    try:
        cursor = conn.cursor()
        update_query = "UPDATE Players SET Number = ? WHERE player_id = ?"
        cursor.execute(update_query, (new_number, player_id))
        conn.commit()
        cursor.close()
        print(f"Player with ID {player_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating player: {e}")

# Updating coach information
def update_coach_info(conn, coach_id, new_salary):
    try:
        cursor = conn.cursor()
        update_query = "UPDATE Coach SET Salary = ? WHERE coach_id = ?"
        cursor.execute(update_query, (new_salary, coach_id))
        conn.commit()
        cursor.close()
        print(f"Coach with ID {coach_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating coach: {e}")

# Updating game information
def update_game_info(conn, game_id, new_location):
    try:
        cursor = conn.cursor()
        update_query = "UPDATE Game SET Location = ? WHERE game_id = ?"
        cursor.execute(update_query, (new_location, game_id))
        conn.commit()
        cursor.close()
        print(f"Game with ID {game_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating game: {e}")

# Delete player by player ID
def delete_player(conn, player_id):
    try:
        cursor = conn.cursor()
        delete_query = "DELETE FROM Players WHERE player_id = ?"
        cursor.execute(delete_query, (player_id,))
        conn.commit()
        cursor.close()
        print(f"Player with ID {player_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting player: {e}")

# User to delete coach by coach ID
def delete_coach(conn, coach_id):
    try:
        cursor = conn.cursor()
        delete_query = "DELETE FROM Coach WHERE coach_id = ?"
        cursor.execute(delete_query, (coach_id,))
        conn.commit()
        cursor.close()
        print(f"Coach with ID {coach_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting coach: {e}")

# User will be able to delete game by game ID
def delete_game(conn, game_id):
    try:
        cursor = conn.cursor()
        delete_query = "DELETE FROM Game WHERE game_id = ?"
        cursor.execute(delete_query, (game_id,))
        conn.commit()
        cursor.close()
        print(f"Game with ID {game_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting game: {e}")

# User will be able to view information on coaches
def display_coaches(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Coach")
    coaches = cursor.fetchall()
    cursor.close()

    if coaches:
        print("\nAll Coaches:")
        for coach in coaches:
            print(coach)
    else:
        print("No coaches found.")

# Main function to run the program
def main():
    db_path = r'C:\Users\UchenduK\OneDrive - Version 1\Documents\workspace\Python\DBSQLLITE\matchgame.db'
    conn = connect_to_db(db_path)
    
    while True:
        print("\nMenu:")
        print("1. Retrieve coach information by name")
        print("2. Retrieve player information by player ID")
        print("3. Retrieve game information by game ID")
        print("4. Update player information")
        print("5. Update coach information")
        print("6. Update game information")
        print("7. Delete player by player ID")
        print("8. Delete coach by coach ID")
        print("9. Delete game by game ID")
        print("10. View all coaches")
        print("11. Exit")
        
        choice = input("Enter your choice (1-11): ")
        
        if choice == '1':
            coach_name = input("Enter coach's first name: ")
            coach_info = retrieve_coach_info(conn, coach_name)
            if coach_info:
                print("\nCoach found:")
                print(coach_info)
            else:
                print(f"No coach found with the name '{coach_name}'.")
        
        elif choice == '2':
            player_id = input("Enter player ID: ")
            player_info = retrieve_player_info(conn, player_id)
            if player_info:
                print("\nPlayer found:")
                print(player_info)
            else:
                print(f"No player found with ID '{player_id}'.")
        
        elif choice == '3':
            game_id = input("Enter game ID: ")
            game_info = retrieve_game_info(conn, game_id)
            if game_info:
                print("\nGame found:")
                print(game_info)
            else:
                print(f"No game found with ID '{game_id}'.")
        
        elif choice == '4':
            player_id = input("Enter player ID to update: ")
            new_number = input("Enter new player number: ")
            update_player_info(conn, player_id, new_number)
        
        elif choice == '5':
            coach_id = input("Enter coach ID to update: ")
            new_salary = input("Enter new coach salary: ")
            update_coach_info(conn, coach_id, new_salary)
        
        elif choice == '6':
            game_id = input("Enter game ID to update: ")
            new_location = input("Enter new game location: ")
            update_game_info(conn, game_id, new_location)
        
        elif choice == '7':
            player_id = input("Enter player ID to delete: ")
            delete_player(conn, player_id)
        
        elif choice == '8':
            coach_id = input("Enter coach ID to delete: ")
            delete_coach(conn, coach_id)
        
        elif choice == '9':
            game_id = input("Enter game ID to delete: ")
            delete_game(conn, game_id)
        
        elif choice == '10':
            display_coaches(conn)
        
        elif choice == '11':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

    conn.close()

if __name__ == "__main__":
    main()
