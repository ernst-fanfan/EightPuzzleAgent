import random


class SlidePuzzle:
    states: list
    possible_moves: list
    end_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    heuristic_score: int
    blank_index: int

    def __init__(self, start_state=None):
        if start_state is not None:
            self.states = start_state
        else:
            self.random_state_loader()
            self.states[-1][1] = self.calcHeuristics()

    def calcHeuristics(self, current_state=None):
        heuristic_score = 0
        if current_state is None:
            current_state = self.states[-1][0]

        for index in range(9):
            heuristic_score += abs(current_state[index] - index)
        return heuristic_score

    def possibleMoves(self):
        current_state = self.states[-1][0]
        self.blank_index = current_state.index(0)
        moves = []

        # Calculates possible moves
        if self.blank_index - 3 >= 0:
            moves.append(self.blank_index - 3)
        if self.blank_index + 3 <= 8:
            moves.append(self.blank_index + 3)
        if self.blank_index in [1, 2, 4, 5, 7, 8]:
            moves.append(self.blank_index - 1)
        if self.blank_index in [0, 1, 3, 4, 6, 7]:
            moves.append(self.blank_index + 1)

        self.possible_moves = moves

    def selectBestMove(self):
        # Picks best move
        best_heu_score = 100
        best_move = []
        current_state = self.states[-1][0]
        for move in self.possible_moves:
            temp_state = self.move(current_state, move)
            temp_score = self.calcHeuristics(temp_state)
            if temp_score <= best_heu_score:
                if [temp_state, temp_score] not in self.states:
                    best_heu_score = temp_score
                    best_move = temp_state
        self.states.append([best_move, best_heu_score])

    def isEndState(self):
        return self.end_state == self.states[-1][0]

    def random_state_loader(self):
        self.states = [[random.sample(range(9), 9), 0]]

    def displayCurrentState(self):
        current_state = self.states[-1][0]
        moves = len(self.states)
        print(f"Current State of Puzzle (moves = {moves}):")
        for i in range(3):
            s = i * 3
            print(current_state[s:s + 3])
        print(f"Current Heuristic score: {self.states[-1][1]}")
        print()

    def move(self, current_state, move):
        new_state = current_state.copy()
        new_state[self.blank_index] = new_state[move]
        new_state[move] = 0
        return new_state
