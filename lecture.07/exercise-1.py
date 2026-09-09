survey_results = [
    ["Python", "JavaScript", "C++"],          # Participant 1
    ["Python", "JavaScript", "C#"],           # Participant 2
    ["Python", "Java"],                       # Participant 3
    ["Python", "C++", "JavaScript"],          # Participant 4
    ["Python", "JavaScript", "C++", "Java"],  # Participant 5
]

# แปลงข้อมูลของแต่ละคนให้เป็น Set
participant_sets = [set(p) for p in survey_results]

all_chosen = set.intersection(*participant_sets)
print("1. Chosen by all participants:", all_chosen)

from collections import Counter

all_languages = [lang for p in survey_results for lang in set(p)]
counts = Counter(all_languages)

single_participant_langs = {
    lang for lang, count in counts.items() if count == 1
}
print("Chosen by a single participant:", single_participant_langs)

unique_languages = set.union(*participant_sets)
print("Total unique languages:", len(unique_languages))

exactly_two_langs = [lang for lang, count in counts.items() if count == 2]
print("Chosen by exactly two participants:", exactly_two_langs)

same_set_pairs = []
for i in range(len(participant_sets)):
    for j in range(i + 1, len(participant_sets)):
        if participant_sets[i] == participant_sets[j]:
            same_set_pairs.append((f"Participant {i+1}", f"Participant {j+1}"))

print("Participants with identical choices:", same_set_pairs)