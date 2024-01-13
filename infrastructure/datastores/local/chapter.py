from domain.entities.value_objects.chapter import VOChapter, VOChapters


class ChapterRepo:

    def __init__(self) -> None:
        self.chapters = {
            "sorcerer's stone": [
                VOChapter(name="Chapter 01 - The Boy Who Lived", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 02 - The Vanishing Glass", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 03 - The Letters From No One", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 04 - The Keeper of the Keys", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 05 - Diagon Alley", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 06 - The Journey From Platform Nine and Three Quarters", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 07 - The Sorting Hat", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 08 - The Potions Master", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 09 - The Midnight Duel", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 10 - Hallowe'en", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 11 - Quidditch", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 12 - The Mirror of Erised", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 13 - Nicolas Flamel", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 14 - Norbert the Norwegian Ridgeback", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 15 - The Forbidden Forest", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 16 -Through the Trapdoor", book_name="sorcerer's stone"),
                VOChapter(name="Chapter 17 - The Man With Two Faces", book_name="sorcerer's stone"),

                ],
            "chamber of secrets": [
                VOChapter(name="Chapter 01 - The Worst Birthday", book_name="chamber of secrets"),
                VOChapter(name="Chapter 02 - Dobby's Warning", book_name="chamber of secrets"),
                VOChapter(name="Chapter 03 - The Burrow", book_name="chamber of secrets"),
                VOChapter(name="Chapter 04 - At Flourish and Blotts", book_name="chamber of secrets"),
                VOChapter(name="Chapter 05 - The Whomping Willow", book_name="chamber of secrets"),
                VOChapter(name="Chapter 06 - Gilderoy Lockhart", book_name="chamber of secrets"),
                VOChapter(name="Chapter 07 - Mudbloods and Murmurs", book_name="chamber of secrets"),
                VOChapter(name="Chapter 08 - The Deathday Party", book_name="chamber of secrets"),
                VOChapter(name="Chapter 09 - The Writing on the Wall", book_name="chamber of secrets"),
                VOChapter(name="Chapter 10 - The Rogue Bludger", book_name="chamber of secrets"),
                VOChapter(name="Chapter 11 - The Dueling Club", book_name="chamber of secrets"),
                VOChapter(name="Chapter 12 - The Polyjuice Potion", book_name="chamber of secrets"),
                VOChapter(name="Chapter 13 - The Very Secret Diary", book_name="chamber of secrets"),
                VOChapter(name="Chapter 14 - Cornelius Fudge", book_name="chamber of secrets"),
                VOChapter(name="Chapter 15 - Aragog", book_name="chamber of secrets"),
                VOChapter(name="Chapter 16 - The Chamber of Secrets", book_name="chamber of secrets"),
                VOChapter(name="Chapter 17 - The Heir of Slytherin", book_name="chamber of secrets"),
                VOChapter(name="Chapter 18 - Dobby's Reward", book_name="chamber of secrets"),
                ],
            "prisoner of azkaban": [
                VOChapter(name="Chapter 01 - Owl Post", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 02 - Aunt Marge's Big Mistake", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 03 - The Knight Bus", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 04 - The Leaky Cauldron", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 05 - The Dementor", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 06 - Talons And Tea Leaves", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 07 - The Boggart In The Wardrobe", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 08 - Flight Of The Fat Lady", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 09 - Grim Defeat", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 10 - The Marauder's Map", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 11 - The Firebolt", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 12 - The Patronus", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 13 - Gryffindor versus Ravenclaw", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 14 - Snape's Grudge", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 15 - The Quidditch Final", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 16 - Professor Trelawney's Prediction", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 17 - Cat Rat And Dog", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 18 - Moony Wormtail Padfoot and Prongs", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 19 - The Servant of the Lord Voldemort", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 20 - The Dementors Kiss", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 21 - Hermione's Secret", book_name="prisonzer of azkaban"),
                VOChapter(name="Chapter 22 - Owl Post Again", book_name="prisonzer of azkaban"),
                ],
            "goblet of fire": [
                VOChapter(name="Chapter 01 - The Riddle House", book_name="goblet of fire"),
                VOChapter(name="Chapter 02 - The Scar", book_name="goblet of fire"),
                VOChapter(name="Chapter 03 - The Invitation", book_name="goblet of fire"),
                VOChapter(name="Chapter 04 - Back to the Burrow", book_name="goblet of fire"),
                VOChapter(name="Chapter 05 - Weasley's Wizarding Wheezes", book_name="goblet of fire"),
                VOChapter(name="Chapter 06 - The Portkey", book_name="goblet of fire"),
                VOChapter(name="Chapter 07 - Bagman and Crouch", book_name="goblet of fire"),
                VOChapter(name="Chapter 08 - The Quidditch World Cup", book_name="goblet of fire"),
                VOChapter(name="Chapter 09 - The Dark Mark", book_name="goblet of fire"),
                VOChapter(name="Chapter 10 - Mayhem at the Ministry", book_name="goblet of fire"),
                VOChapter(name="Chapter 11 - Aboard the Hogwarts Express", book_name="goblet of fire"),
                VOChapter(name="Chapter 12 - The Triwizard Tournament", book_name="goblet of fire"),
                VOChapter(name="Chapter 13 - Mad Eye Moody", book_name="goblet of fire"),
                VOChapter(name="Chapter 14 - The Unforgivable Curses", book_name="goblet of fire"),
                VOChapter(name="Chapter 15 - Beauxbatons and Durmstrang", book_name="goblet of fire"),
                VOChapter(name="Chapter 16 - The Goblet of Fire", book_name="goblet of fire"),
                VOChapter(name="Chapter 17 - The Four Champions", book_name="goblet of fire"),
                VOChapter(name="Chapter 18 - The Weighing of the Wands", book_name="goblet of fire"),
                VOChapter(name="Chapter 19 - The Hungarian Horntail", book_name="goblet of fire"),
                VOChapter(name="Chapter 20 - The First Task", book_name="goblet of fire"),
                VOChapter(name="Chapter 21 - The House Elf Liberation Front", book_name="goblet of fire"),
                VOChapter(name="Chapter 22 - The Unexpected Task", book_name="goblet of fire"),
                VOChapter(name="Chapter 23 - The Yule Ball", book_name="goblet of fire"),
                VOChapter(name="Chapter 24 - Rita Skeeter's Scoop", book_name="goblet of fire"),
                VOChapter(name="Chapter 25 - The Egg and the Eye", book_name="goblet of fire"),
                VOChapter(name="Chapter 26 - The Second Task", book_name="goblet of fire"),
                VOChapter(name="Chapter 27 - Padfoot Returns", book_name="goblet of fire"),
                VOChapter(name="Chapter 28 - The Madness of Mr Crouch", book_name="goblet of fire"),
                VOChapter(name="Chapter 29 - The Dream", book_name="goblet of fire"),
                VOChapter(name="Chapter 30 - The Pensieve", book_name="goblet of fire"),
                VOChapter(name="Chapter 31 - The Third Task", book_name="goblet of fire"),
                VOChapter(name="Chapter 32 - Flesh Blood and Bone", book_name="goblet of fire"),
                VOChapter(name="Chapter 33 - The Death Eaters", book_name="goblet of fire"),
                VOChapter(name="Chapter 34 - Priori Incantatem", book_name="goblet of fire"),
                VOChapter(name="Chapter 35 - Veritaserum", book_name="goblet of fire"),
                VOChapter(name="Chapter 36 - The Parting of the Ways", book_name="goblet of fire"),
                VOChapter(name="Chapter 37 - The Beginning", book_name="goblet of fire"),
                ],
            "order of the pheonix": [
                VOChapter(name="Chapter 01 - Dudley Demented", book_name="order of the pheonix"),
                VOChapter(name="Chapter 02 - A Peck of Owls", book_name="order of the pheonix"),
                VOChapter(name="Chapter 03 - The Advance Guard", book_name="order of the pheonix"),
                VOChapter(name="Chapter 04 - Number Twelve Grimmauld Place", book_name="order of the pheonix"),
                VOChapter(name="Chapter 05 - The Order of the Phoenix", book_name="order of the pheonix"),
                VOChapter(name="Chapter 06 - The Noble and Most Ancient House of Black", book_name="order of the pheonix"),
                VOChapter(name="Chapter 07 - The Ministry of Magic", book_name="order of the pheonix"),
                VOChapter(name="Chapter 08 - The Hearing", book_name="order of the pheonix"),
                VOChapter(name="Chapter 09 - The Woes of Mrs. Weasley", book_name="order of the pheonix"),
                VOChapter(name="Chapter 10 - Luna Lovegood", book_name="order of the pheonix"),
                VOChapter(name="Chapter 11 - The Sorting Hat's New Song", book_name="order of the pheonix"),
                VOChapter(name="Chapter 12 - Professor Umbridge", book_name="order of the pheonix"),
                VOChapter(name="Chapter 13 - Detention With Dolores", book_name="order of the pheonix"),
                VOChapter(name="Chapter 14 - Percy and Padfoot", book_name="order of the pheonix"),
                VOChapter(name="Chapter 15 - The Hogwarts High Inquisitor", book_name="order of the pheonix"),
                VOChapter(name="Chapter 16 - In The Hog's Head", book_name="order of the pheonix"),
                VOChapter(name="Chapter 17 - Educational Decree Number Twenty-Four", book_name="order of the pheonix"),
                VOChapter(name="Chapter 18 - Dumbledore's Army", book_name="order of the pheonix"),
                VOChapter(name="Chapter 19 - The Lion and the Serpent", book_name="order of the pheonix"),
                VOChapter(name="Chapter 20 - Hagrid's Tale", book_name="order of the pheonix"),
                VOChapter(name="Chapter 21 - The Eye of the Snake", book_name="order of the pheonix"),
                VOChapter(name="Chapter 22 - St. Mungo's Hospital for Magical Maladies and Injuries", book_name="order of the pheonix"),
                VOChapter(name="Chapter 23 - Christmas on the Closed Ward", book_name="order of the pheonix"),
                VOChapter(name="Chapter 24 - Occlumency", book_name="order of the pheonix"),
                VOChapter(name="Chapter 25 - The Beetle at Bay", book_name="order of the pheonix"),
                VOChapter(name="Chapter 26 - Seen and Unforeseen", book_name="order of the pheonix"),
                VOChapter(name="Chapter 27 - The Centaur and the Sneak", book_name="order of the pheonix"),
                VOChapter(name="Chapter 28 - Snape's Worst Memory", book_name="order of the pheonix"),
                VOChapter(name="Chapter 29 - Career Advice", book_name="order of the pheonix"),
                VOChapter(name="Chapter 30 - Grawp", book_name="order of the pheonix"),
                VOChapter(name="Chapter 31 - O.W.L.S", book_name="order of the pheonix"),
                VOChapter(name="Chapter 32 - Out of the Fire", book_name="order of the pheonix"),
                VOChapter(name="Chapter 33 - Fight and Flight", book_name="order of the pheonix"),
                VOChapter(name="Chapter 34 - The Department of Mysteries", book_name="order of the pheonix"),
                VOChapter(name="Chapter 35 - Beyond the Veil", book_name="order of the pheonix"),
                VOChapter(name="Chapter 36 - The Only One He Ever Feared", book_name="order of the pheonix"),
                VOChapter(name="Chapter 37 - The Lost Prophecy", book_name="order of the pheonix"),
                VOChapter(name="Chapter 38 - The Second War Begins", book_name="order of the pheonix"),
                ],
            "half blood prince": [
                VOChapter(name="Chapter 01 - The Other Minister", book_name="half blood prince"),
                VOChapter(name="Chapter 02 - Spinner's End", book_name="half blood prince"),
                VOChapter(name="Chapter 03 - Will and Won't", book_name="half blood prince"),
                VOChapter(name="Chapter 04 - Horace Slughorn", book_name="half blood prince"),
                VOChapter(name="Chapter 05 - An Excess of Phlegm", book_name="half blood prince"),
                VOChapter(name="Chapter 06 - Draco's Detour", book_name="half blood prince"),
                VOChapter(name="Chapter 07 - The Slug Club", book_name="half blood prince"),
                VOChapter(name="Chapter 08 - Snape Victorious", book_name="half blood prince"),
                VOChapter(name="Chapter 09 - The Half-Blood Prince", book_name="half blood prince"),
                VOChapter(name="Chapter 10 - The House of Gaunt", book_name="half blood prince"),
                VOChapter(name="Chapter 11 - Hermione’s Helping Hand", book_name="half blood prince"),
                VOChapter(name="Chapter 12 - Silver and Opals", book_name="half blood prince"),
                VOChapter(name="Chapter 13 - The Secret Riddle", book_name="half blood prince"),
                VOChapter(name="Chapter 14 - Felix Felicis", book_name="half blood prince"),
                VOChapter(name="Chapter 15 - The Unbreakable Vow", book_name="half blood prince"),
                VOChapter(name="Chapter 16 - A Very Frosty Christmas", book_name="half blood prince"),
                VOChapter(name="Chapter 17 - A Sluggish Memory", book_name="half blood prince"),
                VOChapter(name="Chapter 18 - Birthday Surprises", book_name="half blood prince"),
                VOChapter(name="Chapter 19 - Elf Tails", book_name="half blood prince"),
                VOChapter(name="Chapter 20 - Lord Voldemort’s Request", book_name="half blood prince"),
                VOChapter(name="Chapter 21 - The Unknowable Room", book_name="half blood prince"),
                VOChapter(name="Chapter 22 - After the Burial", book_name="half blood prince"),
                VOChapter(name="Chapter 23 - Horcruxes", book_name="half blood prince"),
                VOChapter(name="Chapter 24 - Sectumsempra", book_name="half blood prince"),
                VOChapter(name="Chapter 25 - The Seer Overhead", book_name="half blood prince"),
                VOChapter(name="Chapter 26 - The Cave", book_name="half blood prince"),
                VOChapter(name="Chapter 27 - The Lightning-Struck Tower", book_name="half blood prince"),
                VOChapter(name="Chapter 28 - Flight of the Prince", book_name="half blood prince"),
                VOChapter(name="Chapter 29 - The Phoenix Lament", book_name="half blood prince"),
                VOChapter(name="Chapter 30 - The White Tomb", book_name="half blood prince"),
                ],
            "deathly hallows": [
                VOChapter(name="Chapter 01 - The Dark Lord Ascending", book_name="deathly hallows"),
                VOChapter(name="Chapter 02 - In Memoriam", book_name="deathly hallows"),
                VOChapter(name="Chapter 03 - The Dursleys Departing", book_name="deathly hallows"),
                VOChapter(name="Chapter 04 - The Seven Potters", book_name="deathly hallows"),
                VOChapter(name="Chapter 05 - Fallen Warrior", book_name="deathly hallows"),
                VOChapter(name="Chapter 06 - The Goul in Pajamas", book_name="deathly hallows"),
                VOChapter(name="Chapter 07 - The Will of Albus Dumbledore", book_name="deathly hallows"),
                VOChapter(name="Chapter 08 - The Wedding", book_name="deathly hallows"),
                VOChapter(name="Chapter 09 - A Place to Hide", book_name="deathly hallows"),
                VOChapter(name="Chapter 10 - Kreacher's Tale", book_name="deathly hallows"),
                VOChapter(name="Chapter 11 - The Bribe", book_name="deathly hallows"),
                VOChapter(name="Chapter 12 - Magic is Might", book_name="deathly hallows"),
                VOChapter(name="Chapter 13 - The Muggle-born Registration Commission", book_name="deathly hallows"),
                VOChapter(name="Chapter 14 - The Thief", book_name="deathly hallows"),
                VOChapter(name="Chapter 15 - The Goblin's Revenge", book_name="deathly hallows"),
                VOChapter(name="Chapter 16 - Godric's Hollow", book_name="deathly hallows"),
                VOChapter(name="Chapter 17 - Bathilda's Secret", book_name="deathly hallows"),
                VOChapter(name="Chapter 18 - The Life and Lies of Albus Dumbledore", book_name="deathly hallows"),
                VOChapter(name="Chapter 19 - The Silver Doe", book_name="deathly hallows"),
                VOChapter(name="Chapter 20 - Xenophilius Lovegood", book_name="deathly hallows"),
                VOChapter(name="Chapter 21 - The Tale of the Three Borthers", book_name="deathly hallows"),
                VOChapter(name="Chapter 22 - The Deathly Hallows", book_name="deathly hallows"),
                VOChapter(name="Chapter 23 - Malfoy Manor", book_name="deathly hallows"),
                VOChapter(name="Chapter 24 - The Wandmaker", book_name="deathly hallows"),
                VOChapter(name="Chapter 25 - Shell Cottage", book_name="deathly hallows"),
                VOChapter(name="Chapter 26 - Gringotts", book_name="deathly hallows"),
                VOChapter(name="Chapter 27 - The Final Hiding Place", book_name="deathly hallows"),
                VOChapter(name="Chapter 28 - The Missing Mirror", book_name="deathly hallows"),
                VOChapter(name="Chapter 29 - The Lost Diadem", book_name="deathly hallows"),
                VOChapter(name="Chapter 30 - The Sacking of Severus Snape", book_name="deathly hallows"),
                VOChapter(name="Chapter 31 - The Battle of Hogwarts", book_name="deathly hallows"),
                VOChapter(name="Chapter 32 - The Elder Wand", book_name="deathly hallows"),
                VOChapter(name="Chapter 33 - The Prince's Tale", book_name="deathly hallows"),
                VOChapter(name="Chapter 34 - The Forest Again", book_name="deathly hallows"),
                VOChapter(name="Chapter 35 - King's Cross", book_name="deathly hallows"),
                VOChapter(name="Chapter 36 - The Flaw in the Plan", book_name="deathly hallows"),
                VOChapter(name="Epilogue - Nineteen Years Later", book_name="deathly hallows"),
                ]
        }

    def get_all(self, book_name: str) -> list[VOChapter]:
        return self.chapters[book_name]

    def add_chapters(self, chapters: VOChapters) -> list[VOChapter]:
        ...