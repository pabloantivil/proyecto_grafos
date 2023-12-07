def emparejamiento(self):
    # Se guardan en una lista todos sin pareja
    free_people = list(self.grafo.keys())
    # Diccionario de parejas momentaneas
    matches = {}

    while free_people:
        man = free_people[0]
        preferences = self.grafo[man]
        for woman in preferences:
            woman_preferences = self.grafo[woman]
            if woman not in matches.values():
                matches[man] = woman
                free_people.remove(man)
                free_people.remove(woman)
                break
            else:
                current_partner = [
                    k for k, v in matches.items() if v == woman][0]
                if woman_preferences.index(man) < woman_preferences.index(current_partner):
                    free_people.append(current_partner)
                    matches[man] = woman
                    free_people.remove(man)
                    break

    for man, woman in matches.items():
        print(f"{man} - {woman}")
