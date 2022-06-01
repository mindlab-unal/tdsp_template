FROM node:16 as tdsp

WORKDIR /home/node/app

COPY package*.json ./

RUN yarn

COPY . .

CMD ["yarn", "dev"]

FROM tdsp as production

ENV NODE_PATH=./build

RUN npm run build
