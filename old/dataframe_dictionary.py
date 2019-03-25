ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])  # Deleting a key-value pair
del ab['Spammer']
print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))
