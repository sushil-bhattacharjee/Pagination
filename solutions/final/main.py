from messenger import Messenger

if __name__ == "__main__":
    msg = Messenger()
    msg.set_room_id()

    # Get first page
    print('GET FIRST PAGE') 
    msg.get_messages()
    msg.print_current_page()

    page_number = 1
    while page_number <= 3 and msg.has_next_page() is True:
        print(f'MESSAGES ON PAGE {page_number}')
        msg.get_messages()
        msg.print_current_page()
        page_number += 1

    # Reset cursor to first page   
    print('RESET TO FIRST PAGE')
    msg.reset_cursor()
    print('GET FIRST PAGE')
    msg.get_messages()
    msg.print_current_page()