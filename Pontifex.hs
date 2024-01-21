-- Felix Prasanna 2024

import Data.Char (chr, ord)
import Data.List (elemIndex)
import Data.Maybe (fromJust)

-- 52 cards, two jokers
deckSize :: Int
deckSize = 52 + 2

aJoker :: Int
aJoker = deckSize - 1

bJoker :: Int
bJoker = deckSize

startDeck :: [Int]
startDeck = [1..deckSize] -- super secure

test = "iamstealth"
expected = "mxwqbdsrxo"

main :: IO ()
main = do
    print $ expected == encrypt startDeck test
    print $ test == (decrypt startDeck . encrypt startDeck $ test)

encrypt :: [Int] -> String -> String
encrypt deck (c:s) = (i2c . normalize $ c2i c + offset) : encrypt newDeck s
    where (offset, newDeck) = keystreamValue deck
encrypt deck "" = ""

decrypt :: [Int] -> String -> String
decrypt deck (c:s) = (i2c . normalize $ c2i c - offset) : decrypt newDeck s
    where (offset, newDeck) = keystreamValue deck
decrypt deck "" = ""

c2i :: Char -> Int
c2i = flip (-) 96 . ord

i2c :: Int -> Char
i2c = chr . (+) 96 

-- Bring offseted character into the range 1..26
normalize :: Int -> Int
normalize i = if rem == 0 then 26 else rem
    where
        -- the smallest multiple of 26 that is larger than the largest offset,
        -- the decksize, so that we know we're dealing with positive numbers.
        -- also, completely readable arithmetic vv <3
        positifier = (*) 26 . (+) 1 . fst $ quotRem deckSize 26
        rem = (i + positifier) `mod` 26

-- The value of a card. Both jokers count as # of non-joker cards + 1.
value :: Int -> Int
value = min (deckSize - 2 + 1)

-- Move the joker at the given position down one spot. If it is the last card,
-- place it second from the top.
rotateJoker :: Int -> [Int] -> [Int]
rotateJoker pos deck =
  if jokerPos == deckSize - 1
    then -- joker is last card in deck, rotate to second from top
      head deck : pos : take (deckSize - 2) (drop 1 deck)
    else -- joker is not last, swap it with the next card
      take jokerPos deck ++ [deck !! (jokerPos + 1)] ++ [pos] ++ drop (jokerPos + 2) deck
  where
    jokerPos = fromJust (elemIndex pos deck)

-- Perform a triple cut. Move all cards on top of the first joker to below the
-- second joker, and all cards below the second joker to above the first joker.
tripleCut :: Int -> Int -> [Int] -> [Int]
tripleCut joker1 joker2 deck =
  drop (second + 1) deck
    ++ drop first (take (second + 1) deck)
    ++ take first deck
  where
    jokerIndex1 = fromJust (elemIndex joker1 deck)
    jokerIndex2 = fromJust (elemIndex joker2 deck)
    first = min jokerIndex1 jokerIndex2
    second = max jokerIndex1 jokerIndex2

-- Perform a count cut. Move the number of cards represented by the bottom card
-- from the top of the deck to just above the bottom card.
countCut :: [Int] -> [Int]
countCut deck =
  (take (deckSize - count - 1) (drop count deck) ++ take count deck) ++ [last deck]
  where
    count = value . last $ deck

-- Get the next keystream value and deck arrangement out of a deck.
keystreamValue :: [Int] -> (Int, [Int])
keystreamValue deck =
  if shuffled !! index > deckSize - 2
    then keystreamValue shuffled
    else (shuffled !! index, shuffled)
  where
    shuffled =
      countCut
        . tripleCut aJoker bJoker
        . rotateJoker bJoker
        . rotateJoker bJoker
        . rotateJoker aJoker
        $ deck

    index = value (head shuffled)
