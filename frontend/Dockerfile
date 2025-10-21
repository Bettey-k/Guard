FROM node:20-bullseye

WORKDIR /app

# Copy package files FIRST so Docker installs dependencies properly
COPY dashboard/package*.json ./

# Install dependencies (this will include tailwindcss)
RUN npm install

# Now copy the rest of the project
COPY dashboard .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0"]
