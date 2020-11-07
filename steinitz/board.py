from tkinter import Tk, Frame, IntVar, PhotoImage, Radiobutton
from steinitz.utils import rsc, setup, algebraic, side
from os.path import join

class Board(Frame):
    """ The graphic board class """

    def __init__(self, root, send_move, color=('gray', 'brown'), 
                       shape=rsc('style'), width=76, height=76, **args):

        Frame.__init__(self, master=root, **args)
        
        # This is a function. Whenever the user
        # makes a move it is called with the move.
        self.send_move  = send_move
        self.color      = color
        self.width      = width
        self.height     = height
        self.shape      = shape
        self.shape_size = 6
        
        # A dict that maps the board pieces to pictures.
        self.setup_mapping()
        self.initialize()

        POS = ['rnbqkbnr', 
               'pppppppp', 
               '--------', 
               '--------', 
               '--------', 
               '--------', 
               'PPPPPPPP', 
               'RNBQKBNR']
    
        self.update_position(POS, 1)



        """ Initialize a matrix which contains all the images """

    def setup_mapping(self):
        shape_size = str(self.shape_size)
        self.mapping = {
                        # White pawn.
                        'P':join(self.shape, shape_size, 'wp.gif'),
                        # White rook.
                        'R':join(self.shape, shape_size, 'wr.gif'),
                        # White bishop.
                        'B':join(self.shape, shape_size, 'wb.gif'),
                        # White queen.
                        'Q':join(self.shape, shape_size, 'wq.gif'),
                        # White knight.
                        'N':join(self.shape, shape_size, 'wn.gif'),
                        # White king.
                        'K':join(self.shape, shape_size, 'wk.gif'),
                        # Black pawn.
                        'p':join(self.shape, shape_size, 'bp.gif'),
                        # Black rook.
                        'r':join(self.shape, shape_size, 'br.gif'),
                        # Black bishop.
                        'b':join(self.shape, shape_size, 'bb.gif'),
                        # Black queen.
                        'q':join(self.shape, shape_size, 'bq.gif'),
                        # Black knight.
                        'n':join(self.shape, shape_size, 'bn.gif'),
                        # Black king.
                        'k':join(self.shape, shape_size, 'bk.gif'),
                        # It mapps '-' to ''
                        # so it is basically NO PICTURE.
                        '-':''
                        }

    def initialize(self):
        """ This function initializes the board. """

        # We will use this IntVar to mean a square selection.
        self.square = IntVar()

        # This will contain a dict of images and squares.
        self.base = dict()
        
        # We just set up the variables.
        for indi in range(8):
            for indj in range(8):
        # We will hold the pieces into a PhotoImage object.
                img = PhotoImage()
        # Every square is just a RadioButton.
                square = Radiobutton(master      = self, 
                                     width       = self.width, 
                                     height      = self.height, 
                                     image       = img,
                                     indicatoron = 0, 
                                     value       = indi * 8 + indj,
                                     # When one clicks on a square it calls
                                     # self.handle that will store the initial
                                     # square.
                                     command     = lambda move=(indi, indj): self.handle(move),
                                     variable    = self.square,
                                     # It determines the square colour.
                                     background  = setup(indi, indj, self.color))

                square.grid(row = indi, column=indj)
                self.base[indi, indj] = (img, square)
        
        # It holds a initial square when it hasn't selected
        # any square.
        self.state = None

    def handle(self, move):
        """ Called when an user clicks on the board
        and selects a square.
        """

        # If there is no initial square selected
        # we just save it to use later.
        if not self.state:
            self.state = move
        else:
        # If it has a selected square then we have a complete move
        # it is time to call self.send_move with the initial
        # and actual square selection.
            coord = algebraic(self.state, move, self.flip)
            self.send_move(coord)

        # We restore the state to None.
        # Since we have a complete move.
            self.state = None
        # It takes off the RadioButton variable.
            self.square.set(None)

    def update_position(self, style12, flip):
        """ This function is called to update the board position
        based on a style12 string.
        """
        for indi in range(8):
            for indj in range(8):
                # It determines the coordinates in style12
                # notation.
                coord = side((indi, indj), flip)
                x, y = coord

                # We then have the chunk that determines
                # the type of piece.
                chunk = style12[x][y]
                # As we saved the image attributes of the square
                # in the self.base we now can update the image.
                img, square = self.base[indi, indj]
                img.configure(file=self.mapping[chunk])
                # If it is '-' then it has no image.
                if chunk == '-':
                    img.blank()

        # We save the flip to use in self.handle.
        self.style12 = style12
        self.flip = flip

    def incheight(self, rate=2):
        """ It increases square height. """
        for indi in range(8):
            for indj in range(8):
                img, square = self.base[indi, indj]
        # It gets the actual height and adds
        # rate to it.
                h = square.cget('height')
                hn = int(str(h)) + rate
                square.configure(height = hn)

    def decheight(self, rate=2):
        """ It decreases square height. """
        for indi in range(8):
            for indj in range(8):
                img, square = self.base[indi, indj]
        # It gets the actual height and
        # sub rate from it.
                h = square.cget('height')
                hn = int(str(h)) - rate
                square.configure(height = hn)

    def incwidth(self, rate=2):
        """ It increases square width. """
        for indi in range(8):
            for indj in range(8):
                img, square = self.base[indi, indj]
                h = square.cget('width')
                hn = int(str(h)) + rate
                square.configure(width = hn)

    def decwidth(self, rate=2):
        """ It decreases square width. """
        for indi in range(8):
            for indj in range(8):
                img, square = self.base[indi, indj]
                h = square.cget('width')
                hn = int(str(h)) - rate
                square.configure(width = hn)

    def update_shape(self):
        self.setup_mapping()
        self.update_position(self.style12, self.flip)

    def incshape(self):
        """ I should review it. """
        self.shape_size = self.shape_size + 1
        self.update_shape()

    def decshape(self):
        """ I should review it. When one decreases a lot it 
            throws exception."""

        self.shape_size = self.shape_size - 1
        self.update_shape()

    def chshape(self):
        pass


if __name__ == '__main__':
    root = Tk()
    app = Board(root)
    pos = ['rnbqkbnr', 
           'pppppppp', 
           '--------', 
           '--------', 
           '--------', 
           '--------', 
           'PPPPPPPP', 
           'RNBQKBNR']

    app.update_position(pos, 1)

    app.pack(expand=True)
    root.mainloop()








