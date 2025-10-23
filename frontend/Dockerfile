# 1️⃣ Use Node.js official image
FROM node:22-alpine
WORKDIR /app

# 2️⃣ Copy only package files first (for caching)
COPY dashboard/package*.json ./

# 3️⃣ Install dependencies
RUN npm install

# 4️⃣ Copy all dashboard source code
COPY dashboard .

# 5️⃣ Expose Next.js port
EXPOSE 3000

# 6️⃣ Start development server (bind to all interfaces)
CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0"]