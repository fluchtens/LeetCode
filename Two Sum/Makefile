NAME = solution

CC = c++
CFLAGS = -Wall -Wextra -Werror
RM = rm -f

SRCS = solution.cpp
OBJS = ${SRCS:.cpp=.o}

all: ${NAME}

%.o: %.cpp
	${CC} ${CFLAGS} -c $< -o $@

${NAME}: ${OBJS}
	${CC} ${CFLAGS} ${OBJS} -o ${NAME}

clean:
	${RM} ${OBJS}

fclean: clean
	${RM} ${NAME}

re: fclean all

.PHONY: all clean fclean re
