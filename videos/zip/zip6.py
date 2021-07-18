


def main():
    Ages = [
        'Greg',
        'Marsha',
        'Peter',
        'Jan',
        'Bobby',
        'Cindy'
    ]
    
    rank_dict = dict(map(reversed, enumerate(Ages)))
    
    Ages = sorted(Ages)
    
    Ages = sorted(Ages, key=(lambda e: rank_dict[e]))
    
    return

if __name__ == '__main__':
    main()
        