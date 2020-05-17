import sys

A = [[1, 1, 1, 1, 1],   # Ο λαβύρινθος
     [1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1]]

MA = [[[5, 1]]]         # Αρχικοποιώ το Μέτωπο Αναζήτησης με το σημείο έναρξης
FinalState = [5, 3]     # Το τελικό σημείο για να ολοκληρωθεί η διαδρομή
BestCost = sys.maxsize  # Αρχικοποιώ το κόστος με την μέγιστη τιμή
BestRoute = []          # Εδώ κρατάω την καλύτερη διαδρομή μέχρι τώρα
Katastasi = []          # Η διαδρομή που κάναμε μέχρι τώρα
Paidia = []             # Σε κάθε loop εδώ θα βάζουμε τις καταστάσεις παιδιά
loop = 0                # Μετρητής επαναλήψεων


def find_children(katastasi1):         # Το function που βρίσκει τις καταστάσεις παιδιά
    x = y = 0
    newcoords = []
    children_states = []
    if len(katastasi1) == 1:           # Αν η μέχρι τώρα διαδρομή έχει μόνο ένα σημείο,
        newcoords = katastasi1[0]      # το παίρνουμε αυτό για επέκταση της διαδρομής
        x = newcoords[1]
        y = newcoords[0]
    elif len(katastasi1) > 1:          # Αν όμως η διαδρομή έχει περισσότερα σημεία,
        newcoords = katastasi1[-1]     # παίρνουμε το τελευταίο για επέκταση της διαδρομής (με το [-1])
        x = newcoords[1]
        y = newcoords[0]
    print('Frontier: '+str(MA))
    print('We are at: ' + str(newcoords))
    print('Route until now: ' + str(katastasi1))  # Εδώ γίνεται ο έλεγχος για το κλάδεμα. Συγκρίνω το len(katastasi1)
    if len(katastasi1) < BestCost:               # αντί ( len(katastasi1) -1 ) γιατί έτσι έχουμε το κόστος της
        print('----------- Moves -----------')  # διαδρομής + 1, οπότε βλέπουμε αν θα φτάσει το best cost με οποιαδήποτε
        # north                                 # επιπλέον κίνηση.
        if y - 1 >= 0:  # Ελέγχω αν το y-1>=0 γιατί αν γίνει αρνητικός θα παίρνει y από το τέλος της λίστας του λαβύρινθου
            if A[y - 1][x] == 0:         # Αν ισούται με 0 σημαίνει ότι μπορεί να πάει στο κουτάκι βόρεια
                child_north_x = x
                child_north_y = y - 1
                if [y - 1, x] not in katastasi1:                        # Αν υπάρχει ήδη στην διαδρομή δεν το παίρνουμε
                    child_north = katastasi1 + [[child_north_y, child_north_x]]  # Βάζουμε το νέο σημείο στο τέλος της
                    children_states.append(child_north)             # διαδρομής και την βάζουμε στις καταστάσεις παιδιά
                    print("| Can Go North              |")
                else:
                    print("| Already been to North!    |")
            else:
                print("| Can't go North            |")
        else:
            print('| Already at edge of north! |')

        try:              # Εδώ αντί για if χρησιμοποιώ Exception Handling γιατί αν y+1 > max y , θα βγάλει IndexError
            # south       # το οποίο στην ουσία σημαίνει ότι είναι ήδη στο πιο νότιο σημείο του λαβυρίνθου.
            if A[y + 1][x] == 0:        # Τα υπόλοιπα είναι αντίστοιχα με τα πάνω
                child_south_x = x
                child_south_y = y + 1
                if [y + 1, x] not in katastasi1:
                    child_south = katastasi1 + [[child_south_y, child_south_x]]
                    children_states.append(child_south)
                    print("| Can Go South              |")
                else:
                    print("| Already been to South!    |")
            else:
                print("| Can't go South            |")
        except IndexError:
            print('| Already at edge of south! |')

        try:                # Είναι αντίστοιχα με τα πάνω
            # east
            if A[y][x + 1] == 0:
                child_east_x = x + 1
                child_east_y = y
                if [y, x + 1] not in katastasi1:
                    child_east = katastasi1 + [[child_east_y, child_east_x]]
                    children_states.append(child_east)
                    print("| Can Go East               |")
                else:
                    print("| Already been to East!     |")
            else:
                print("| Can't go East             |")
        except IndexError:
            print('|Already at edge of east! |')

        if x - 1 >= 0:              # Είναι αντίστοιχα με τα πάνω
            if A[y][x - 1] == 0:
                child_west_x = x - 1
                child_west_y = y
                if [y, x - 1] not in katastasi1:
                    child_west = katastasi1 + [[child_west_y, child_west_x]]
                    children_states.append(child_west)
                    print("| Can Go West               |")
                else:
                    print("| Already been to West!     |")
            else:
                print("| Can't go West             |")
        else:
            print('| Already at edge of west!  |')

        print('-----------------------------')
    else:
        print('Branch Cut! Best Cost until now: ' + str(BestCost))
    return children_states


while len(MA) != 0:    # Loop μέχρι να αδιάσει το Μέτωπο αναζήτησης
    loop += 1
    print("\nLoop number: " + str(loop))
    Katastasi = MA[0]                      # Παίρνουμε σαν κατάσταση το πρώτο από το Μέτωπο Αναζήτησης.
    MA.pop(0)                              # Αφαιρούμε από το ΜΑ το πρώτο.
    if Katastasi[-1] != FinalState:        # Αν το τελευταίο σημείο της κατάστασης δεν ισούται με το [5,3]
        Paidia = find_children(Katastasi)  # Βρίσκουμε τα παιδιά
        MA = Paidia + MA                   # Προσθέτουμε τα παιδιά μπροστά στο μέτωπο αναζήτησης
        Paidia.clear()                     # Αδειάζουμε την λίστα με τα παιδιά
    else:                                  # Αν φτάσαμε στο τελικό σημείο [5,3]
        print('A route has been completed!')
        print('Route: ' + str(Katastasi))
        CurrentCost = len(Katastasi) - 1   # Το κόστος είναι -1 γιατί στην κατάσταση υπάρχει και το αρχικό σημείο [5,1]
        print('Cost for this route: ' + str(CurrentCost))
        if CurrentCost < BestCost:    # Έλεγχος αν το κόστος αυτής της διαδρομής είναι μικρότερο από αυτό που έχουμε ήδη
            BestRoute = Katastasi     # Ανανέωση των τιμών BestRoute και BestCost
            BestCost = CurrentCost

if BestCost == sys.maxsize:         # Αν το κόστος παρέμεινε maxsize, κάτι πήγε λάθος ή δεν μπορει να φτάσει στο [5,3]
    print("Something went wrong, or can't reach Final Coordinates.")
else:
    print("\nEnd of B&B Algorithm.")
    print("Best Route: " + str(BestRoute))
    print("Best Cost: " + str(BestCost))
